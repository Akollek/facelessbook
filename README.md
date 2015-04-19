# FacelessBook

[FacelessBook](http://www.cs.mcgill.ca/~akolle2/)

-----

By Matthew Creme, Amiel Kollek, and Arthur Plis

Note on directory structure:
	- html : contains all template HTML used in the newsfeed functionality
	- data : holds csvs with members and newfeed items 
	- auth: contains login and authentication code, as well as stores keys used for authentication
	- registration : holds code for registering a new user
	- newsfeed : holds code for the newsfeed (posting, viewing more items) and adding friends

### HTML

	Templates are filled out by replacing relevant values in python
### Data
	Contains members.csv and topics.csv. 
	topics.csv has the structure: user\n comment\n image url

### Auth
        When a user logs on, this creates a key, which is written to a file on the sever.
        File has name which is just the user name of the user logging in and is stored in auth/keys/.
	This key is passed along as a hidden value in the form for all other functions of the site and checked against the server.
	logout deletes the key

### Registration 

	Simply adds a user to members.csv

### Newsfeed

htmlHelper.py contains the class which generates all the HTML for the main page. Pulls in base.html, fills in the friends of the current user and the posts. 
Also authenticates the user against the keys.

#### Posting
     Validates that the image url given is 
	- a url that ends in an image extension (just a regex check)
	- checks that there are no faces in the image. (this is done on a separate server since we couldn't install the library on cgi.cs.mcgill.ca properly...)
	- adds all the info to topics.csv and rerenders the main page with htmlHelper

#### Add friend
	Edits members.csv and rerenders with htmlHelper

#### More
	Shows 10 more posts then are already there, and rerenders the page, updating the number of posts to be shown on the next click of "More" by +=10




