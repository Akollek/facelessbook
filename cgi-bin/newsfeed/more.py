#!/usr/bin/python

"""
        more.py
        -------

This script calls calls the newsfeed with more of friends news items
"""

from htmlHelp import *
import cgi

form = cgi.FieldStorage()

key   = form.getvalue('key')
user  = form.getvalue('user') 
items = form.getvalue('items')

print "Content-Type: text/html\n\n"

# get the number of items and render the page with that many items
# 	the items field is changed +=10
generator = HtmlGenerator("bob",key,int(items))
generator.generate_feed_html()
generator.generate_member_html()

# if there are no new items, let the user know
if generator.overflow:
        generator.send_html("There are no new new items!")
else:
        generator.send_html()

