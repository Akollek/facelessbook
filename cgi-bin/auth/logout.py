#!/usr/bin/python

""" 
        logout.py
        --------

Upon logout, the key is deleted
"""

import cgi
import os
from subprocess import call

form = cgi.FieldStorage()

user = form.getvalue('user')
filename = "keys/"+user+".key"

if os.path.exists(filename):
        call(["rm",filename])



print "Content-Type: text/html\n\n"
print "<html><body><body bgcolor=#34A085><font color=\"#5D1B7C\"><p><h4> You have logged out</h4></p><p> Proceed <a href=\"http://cs.mcgill.ca/~akolle2/\">here</a> to log in again </p></font></body>   </html>"

