#!/usr/bin/python

####################################
#              NEWSFEED            #
# -------------------------------- #
# Reads topics.csv backwards and   #
# generates the newsfeed HTML      #
####################################

import sys
import csv
import os

def list_flatten(l):
        return [ e[0] for e in l]  

class Topic:
	"""
		class to ornaize news items	
	"""
        def __init__(self,user,comment,url):
                self.user = user
                self.comment = comment
                self.url = url
        
        def info(self):
                return [self.url,self.comment,self.user]


def authenticate(user,key):
	""" 
		check if the key stored on the server matches the one given by the user
	"""
	filename = "../auth/keys/"+user+".key"
	if not os.path.exists(filename):
		# if the file doesn't exist, then they are not logged on
		return False
        with open(filename,"r") as f:
                cont = f.read().strip()
                return cont == key


class HtmlGenerator:
        """
        class to organize everything to do with HTML generation"
        """
        def __init__(self, user, key, size):
                """
                Function to initilalize the HtmlGenerator class.
                Creates a list of items to be included in the newsfeed from topics.csv
                and reads in all base HTML
                """
                self.user = user 
                self.key = key
                self.auth = authenticate(self.user,self.key) 
                if not self.auth:
                        self.html = "<html><body bgcolor=\"#34A085\"><font color=\"#5D1B7C\"><h1> Authentication error, incorrect key. You may need to sign in again.</h1></font></body></html>"
                        return

                # get base HTML for whole page
                with open("../html/base.html","r") as f:
                        self.html = f.read()

                self.html = self.html.replace("{user}",user)
                
                # get item template HTML
                with open("../html/item.html","r") as f:
                        self.itemHtml = f.read()
               

                # get members
                with open("../data/members.csv","r") as f:
                        reader = csv.reader(f)
                        self.members = [ row[1] for row in reader]
                
                with open("../data/members.csv","r") as f:
                        reader = csv.reader(f)
                        for row in reader:
                                if row[1] == user:
                                        self.friends = row[3:]
                # get news items
                with open("../data/topics.csv","r") as f:
                        rows = [ row.strip() for row in f ]

                items = [ Topic(*rows[i*3:i*3+3]) for i in range(int(len(rows)/3)) ]
                
                items = [ item for item in items if ((item.user in self.friends) or (item.user == self.user)) ]
                
                items.reverse()
                length = len(items)
                if size > length:
                        size = length
                        self.overflow = True
                        self.html = self.html.replace("{submit}","hidden")
                else:
                        self.overflow = False
                        self.html = self.html.replace("{submit}","submit")
                        self.html = self.html.replace("{items}",str(size+10))
                
                # make items list
                self.items = items[:size]

        def generate_feed_html(self):
                if not self.auth:
                        return

                feedHtml = ""
                for item in self.items:
			# format each news item into one long html string
                        feedHtml = feedHtml + self.itemHtml.format(*item.info())
		# add this string the the HTML of the page
                self.html = self.html.replace("{feed}",feedHtml)

        def generate_member_html(self):
                if not self.auth:
                        return
                baseMemberHtml = "<li> <font {1}> {0} </font></li>\n"
                memberHtml = ""
                self.members.remove(self.user) #don't show the current user in the member list
		# for each member, format html with them and add them to a string of HTML
                for member in self.members:
                        memberHtml = memberHtml + baseMemberHtml.format(member,["","color=#ff0000"][member in self.friends]) # colour friends
		
		# add the memeber list to the main HTML
                self.html = self.html.replace("{members}",memberHtml)

                
        def send_html(self,message=""):
		# add an optional message 
                self.html = self.html.replace("{message}",message)
                self.html = self.html.replace("{key}",self.key)
                print self.html
                        








        
