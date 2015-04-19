import cv
import sys
import urllib
import urllib2

"""
facial detection adapted from https://github.com/shantnu/FaceDetect/


NOTE TO MARKER:
--------------

Due to issues installing and using the python module required to perform face detection.
we chose to run a site on a serperate server and do the detection there, sending the result back.
(we received permission to do this)

This was done with flask on Heroku. The deployed code is included in this directory as `app.py`

"""



def validate_image(imageURL):
	
	handler = urllib2.HTTPHandler()	
	opener = urllib2.build_opener(handler)

	url = "https://sleepy-earth-7382.herokuapp.com/validate/"
	data = urllib.urlencode( {'image' : imageURL} )
	
	result = opener.open(url, data=data).read()

	if "No" in result:
		return False
	else:
		return True	

