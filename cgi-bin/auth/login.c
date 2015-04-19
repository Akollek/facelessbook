
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXLENGTHUSER 10 //can be changed
#define MAXLENGTHPASS 10 //can be changed
#define MAXLENGTHNAME 10 //can be changed
#define MINLENGTHPASS 1 //can be changed
#define MINLENGTHUSER 1 //can be changed
#define EXTRALENGTH 32 //cant be changed
#define STARTUSER 9 //cant be changed, refers to the where the username starts in the cgi post
#define STARTPASS 19 //cant be changed, refers to the where the password starts in the cgi post
#define boolean int
#define false 0
#define true 1

boolean validate(char username[], char password[]){
	FILE *file;
	int maxtemplength=MAXLENGTHNAME+MAXLENGTHUSER+MAXLENGTHPASS+3; //2 for commas, 1 for EOF
	char temp[maxtemplength];
	
	//making the sub-string that we will be looking for in members.csv
	char name[MAXLENGTHUSER+MAXLENGTHPASS+3];//2 for commas, 1 for EOF
	snprintf(name, sizeof name, "%s%s%s%s%s%s", ",", username, ",", password,",","\0");
	
	
	//checking if the substring is in members.csv
	if((file=fopen("../data/members.csv","r"))== NULL)
		return false;
	
	while(fgets(temp,maxtemplength,file) != NULL){
		
		//the username and password will start directly after the first comma in members.csv
		int current=0;
		  while(temp[current]!=',')
			current++;
		
		  int current1=0;
		  boolean possible=true;
		
		 
		  while(current1<strlen(name) && (possible)){
			if(temp[current]!=name[current1])
			possible=false;
		
			current++;
			current1++;	
			}
		//if the string is found, indicate this fact
		  if(possible && temp && current1==strlen(name))
			   return true;
		
		}
	return false;
	}

void loginfail(){
	printf("<html>");
	printf("<body bgcolor=#34A085>");
	printf("<font color=#5D1B7C>ERROR:No such username and password exist<br>");
	printf("<a href=\"http://www.cs.mcgill.ca/~akolle2\">Go Back to Login Page</font></a></p>");
	printf("</body>");
	printf("</html>");
}

void loginsuccess(char username[]){
	// set rand seed with time
        srand(time(0));

         // generate a random key
        int key = rand();
        FILE * keyfile;
        char keyfilepath[20 + 10]; // max username + extra for "keys/[...].key\0"

        // generate a filename for the key of this user
        snprintf(keyfilepath, sizeof(keyfilepath), "%s%s%s", "keys/", username, ".key\0");

        // open the keyfile ("w" option destroys contenst if the file exists already
        keyfile = fopen(keyfilepath,"w");

        // write the key to the file and close
        fprintf(keyfile, "%d", key);
        fclose(keyfile);
	
	// print the HTML for the page
	printf("<DOCTYPE html>\n");
        printf("");
        printf("<html>\n");
        printf("        <body>\n");
        printf("                <body bgcolor=\"#34A085\"><font color=\"#5D1B7C\"><p> Thank you for logging in. Please click below to proceed to your newsfeed</p></font>\n");
        printf("                <form action=\"../newsfeed/newsfeed.py\" method=\"POST\">\n");
        printf("                        <input type=\"submit\" value=\"Newsfeed\">\n");
        printf("                        <input type=\"hidden\" name=\"user\" value=\"%s\">\n", username);
        printf("                        <input type=\"hidden\" name=\"key\" value=\"%d\">\n", key);
        printf("                </form>\n");
        printf("        </body>\n");
        printf("</html>\n");

	
	// set a time to delete the key
	char command[20+15]; // username + command length
	snprintf(command, sizeof(command), "%s%s%s", "./timer.sh ", "username", "\0");
	system(command);	
}

void main(){
	char username[MAXLENGTHUSER+1];
	char password[MAXLENGTHPASS+1];
	char data[MAXLENGTHUSER+MAXLENGTHPASS+EXTRALENGTH];
	char c;
	boolean keepgoing=true;
	

	printf("Content-type: text/html\n\n");
	
	int n= atoi(getenv("CONTENT_LENGTH"));
	
	int count=0;
	int current;
		
	//putting the infromation from cgi into an array	
	while((c= getchar())!= EOF && count<MAXLENGTHUSER+MAXLENGTHPASS+EXTRALENGTH){
		data[count]=c;
		count++;}
	data[count]='\0';
	
	if(c!=EOF){
		loginfail();
		keepgoing=false;
	}
	
	//splitting up the data appropriately into username and password
	if(keepgoing){
		count=0;
		c=data[STARTUSER];
		current=STARTUSER;
		
		while (c!='&' && count<MAXLENGTHUSER){
		 	username[count]=c;
		 	current=current++;
		 	c=data[current];
		 	count++;}
		username[count]='\0';
		
		
		if(c!='&' || strlen(username)<MINLENGTHUSER){
			loginfail();
			keepgoing=false;}
	}
	
	if(keepgoing){
		count=0;
		c=data[STARTPASS+strlen(username)];
		current=STARTPASS+strlen(username);
		
		while (c!='&' && count<MAXLENGTHPASS){
		 	password[count]=c;
		 	current=current++;
		 	c=data[current];
		 	count++;}
		
			password[count]='\0';
		
		if(c!='&' || strlen(password)<MINLENGTHPASS){
			loginfail();
			keepgoing=false;}
	}
	
	if(keepgoing){
	if(validate(username,password))
		loginsuccess(username);
	else
		loginfail();
	}
}
