from flask import Flask, render_template, request
import sys
import cv2
import logging
import urllib
import os



########
# Face detection code adapted from https://github.com/shantnu/FaceDetect
########




app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

# ignore this:
#######################
@app.route('/')
def index():
        image = "static/dog.jpg"
        return render_template('index.html',image=image)
#######################



@app.route('/validate/',methods=['POST'])
def facedetect():
        image = request.form['image']
        imagePath = "tmp.png"
        urllib.urlretrieve(image, imagePath)
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags = cv2.cv.CV_HAAR_SCALE_IMAGE
                )
        os.remove(imagePath)

        if len(faces) > 0:
                return "Face"
        else:
                return "No"


if __name__ == "__main__":
        port = int(sys.argv[1])
        app.run(host="0.0.0.0",port=port)





