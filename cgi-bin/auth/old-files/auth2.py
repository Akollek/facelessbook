#!/usr/bin/python
################################################################
#    MAKE KEY                                                  #
# ------------------------------------------------------------ #
# This script is given a username and generates a key, then    #
# runs a timer to destroy the key                              #
################################################################


import subprocess
import os
from random import randint 
import sys

user = sys.argv[1]
key  = str(randint(0,2 ** 32-1))

keyfile = "keys/"+sys.argv[1] + ".key"


if os.path.exists(keyfile):
	os.remove(keyfile)

f = open(keyfile, "wt+")
f.write(key)
f.close()
os.system("./timer.sh "+keyfile+"&")

#subprocess.call(['./timer.sh',keyfile,"&"])

with open("../html/auth.html", "r") as f:
        authHtml = f.read()

authHtml = authHtml.replace("{user}",user)
authHtml = authHtml.replace("{key}",key)

htmlfile = "temp.html"

if os.path.exists(htmlfile):
	os.remove(htmlfile)

with open(htmlfile,"w+") as f:
	f.write(authHtml)
