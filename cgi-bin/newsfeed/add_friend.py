#!/usr/bin/python

"""
add_friend.py
-------------

cgi script to add a friend for a user. Takes the user and edits members.csv
"""


import csv
from htmlHelp import *
import cgi


form = cgi.FieldStorage()

user = form.getvalue('user')
friend = form.getvalue('friend')
key = form.getvalue('key')

def add(array,new_user):
	added = array
	added.append(new_user)
	return added


# first load the csv with appending the new friend on the correct place
with open("../data/members.csv","r") as f:
        reader = csv.reader(f)
        out = []
        for row in reader:
                if row[1] == user:
                        out.append(add(row,friend))
                else:
                        out.append(row)


# rewrite the csv with the new friend
with open("../data/members.csv","w") as f:
        writer = csv.writer(f)
        writer.writerows(out)

print "Content-Type: text/html"


generator = HtmlGenerator(user,key,10)

# give a message appropriate if the friend added exists or not
if friend in generator.members:
	message = "Friend added!"
else: 
	message = "You can't just make up friends, that's so desperate..."


# generate the html for the newsfeed and send it
generator.generate_feed_html()
generator.generate_member_html()
generator.send_html(message)


