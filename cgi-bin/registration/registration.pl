#!/usr/bin/perl
use strict;
use Fcntl;
use CGI ':standard';

my $name = param('name');
my $usr = param('username');
my $psw = param('password');
my $confirm = param('confirm');

# validate the username is of a proper format
foreach($name, $usr, $psw){
    if (index($_,',') != -1 || index($_, '>') != -1 || index($_, '<') != -1 || index($_, ' ') != -1 || index($_, '&') != -1){
        print "Content-Type: text/html\n\n";
        print <<ENDHTML;
<html>
	<body bgcolor=#34A085>
		<b><font color=#FFD768>You can't use any special characters in your name, password and username.</font></b><br>
		<a href="http://www.cs.mcgill.ca/~akolle2/cgi-bin/html/registration.html">Back to registration page</a>
	</body>
</html>
ENDHTML
exit 0;
    }
}

# validate the password and confirmed password are the same
if ($psw ne $confirm){
    print "Content-Type: text/html\n\n";
    print <<ENDHTML;
<html>
	<body bgcolor=#34A085>
		<b><font color=#FFD768>Your password and confirmed password don't match.</font></b><br>
		<a href="http://www.cs.mcgill.ca/~akolle2/cgi-bin/html/registration.html">Back to registration page</a>
	</body>
</html>
ENDHTML
exit 0;
}

# validate the fields are not empty
elsif (!$psw || !$usr || !$psw || !$name){
    print "Content-Type: text/html\n\n";
    print <<ENDHTML;
	<html>
		<body bgcolor=#34A085>
			<b><font color=#FFD768>You left one of the fields empty.</font></b><br>
			<a href="http://www.cs.mcgill.ca/~akolle2/cgi-bin/html/registration.html">Back to registration page</a>
	</body>
</html>
ENDHTML
exit 0;
}

# ensure username doesn't exists
open (my $memberz, "+<", "../data/members.csv");
while (my $line = <$memberz>) {
    chomp $line;
    my @fields = split(",",$line);
    if ($usr eq $fields[1]){
        print "Content-Type: text/html\n\n";
        print <<ENDHTML;
<html>
	<body bgcolor=#34A085>
		<b><font color=#FFD768>Username already exists. Please choose a different username.</font></b><br>
		<a href="http://www.cs.mcgill.ca/~akolle2/cgi-bin/html/registration.html">Back to registration page</a>
	</body>
</html>
ENDHTML
exit 0;
    }
}

# add the user and give them Tom from MySpace as a friend
print $memberz "$name,$usr,$psw,Tom from MySpace\n";
#seek ($memberz, 0, 0);
print "Content-Type: text/html\n\n";
print <<ENDHTML;
	<html>
	<body bgcolor=#34A085>Please sign in to your account at the <a href="http://www.cs.mcgill.ca/~akolle2/"> welcome page</a>
		<center><h1><font color=#FFD768>Congratulations, you are now offically a member of FacelessBook!</font></h1></center><br>
	</body>
</html>
ENDHTML

close ($memberz);

