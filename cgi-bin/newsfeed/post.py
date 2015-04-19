#!/usr/bin/python

"""
        post.py
        ------

        To make a post to the newsfeed

"""

import sys
import os
import csv
import cgi
from htmlHelp import *
from face_detect import *
import urllib
import re
from urllib2 import Request, urlopen, URLError

def check_image(imagePath):
	# check the image url is of a valid format
	URLRegex = re.compile(r'https?://.+/.+\.([pP][nN][gG]|[jJ][pP][gG]|[jJ][pP][eE][gG]|gif)$')
	return URLRegex.match(imagePath)	


form = cgi.FieldStorage()

user     = form.getvalue('user')
comment  = form.getvalue('comment')
image    = form.getvalue('image')
key      = form.getvalue('key')


# to ensure there is no HTML injection
comment = comment.replace("<","&lt;")
comment = comment.replace(">","&gt;");

print "Content-Type: text/html\n\n"

if (not comment) or (not image):
	#validate all fields filled
	message = "Please fill all fields."
elif not check_image(image):
	# valudate the url
	message = "Please enter an image URL, supported formats are png,jpg,jpeg and gif"
else:
	if not validate_image(image):
		# check there are not faces and add/don't add with the appropriate message
		with open("../data/topics.csv",'a') as f:
        		f.write(user+"\n"+comment+"\n"+image+"\n")
		message = "Image added!"
	else:
		message = "Image not added. You tried to upload a face. I said you can't upload faces. Don't test me."


# send the newsfeed page
generator = HtmlGenerator(user,key,10)
generator.generate_feed_html()
generator.generate_member_html()
generator.send_html(message)


