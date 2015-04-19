#!/usr/bin/python

####################################
#              NEWSFEED            #
# -------------------------------- #
# Reads topics.csv backwards and   #
# generates the newsfeed HTML      #
####################################

import sys
import csv
import cgi
import os
from htmlHelp import *


print "Content-Type: text/html\n\n" 

form = cgi.FieldStorage()

key = form.getvalue('key')
user = form.getvalue('user')

generator = HtmlGenerator(user,key,10)
generator.generate_feed_html()
generator.generate_member_html()
generator.send_html()





        
