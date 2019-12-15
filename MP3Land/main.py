#!/usr/bin/env python3
import youtube_dl
import sys
import datetime
import time

# https://pypi.org/project/tinytag/
# https://eyed3.readthedocs.io/en/latest/


import eyed3
from tinytag import TinyTag


from flask import Flask, Response, render_template, request
from flask import send_file
from jinja2 import Template

import random


app = Flask(__name__)


@app.route('/')
def mainland():

	fileName = getRandomString() + ".mp3"

	# Settings for downloading
	ydl_opts = {
		'forcetitle': True,
	    'format': 'bestaudio/best',
	    'postprocessors': [{
	        'key': 'FFmpegExtractAudio',
	        'preferredcodec': 'mp3',
	        'preferredquality': '192',
	    }],
	    'noplaylist' : True,
	    'progress_hooks': [my_hook],
	    'outtmpl': './' + fileName
	}

	# Download from youtube
	# youtube_dl.YoutubeDL(ydl_opts).download(['https://www.youtube.com/watch?v=5ytzbr4SiKE'])


	# USE TINY TAG TO GET ATTRIBUTES
	# fileTags = TinyTag.get(fileName)
	# print('This track is by %s.' % fileTags.artist)


	return render_template('index.html', fileName = fileName)

	#send_file('./helloWorld.mp3', as_attachment=True)





@app.route("/tags", methods=['POST','GET'])
def tags():

	fileName = request.form.get('fileName')

	songTitle = request.form.get('songTitle')
	songTitle = songTitle.capitalize()

	songArtist = request.form.get('songArtist')
	songArtist = upperArtist(songTitle)

	songGenre = request.form.get('songGenre')
	songAlbum = "Musica JD"

	# LOAD THIS FILE
	audio = eyed3.load(fileName)

	audio.initTag()

	

	audio.tag.title = unicode(songTitle)
	audio.tag.artist = unicode(songArtist)
	audio.tag.album_artist = unicode(songArtist)

	# audio.tag.genre = u"ccc"
	audio.tag.album = unicode(songAlbum)
	audio.tag.track = u""

	audio.tag.images.set(3, open('music.png','rb').read(), 'image/png')
	audio.tag.save()





	return Response(songGenre)






def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


# #Download MP3 from Youtube
# def downloadSong(link):









# RETURN ARTIST AS NICE STRING
def upperArtist(string):
	newList = list(string.split(" "))
	newString = ""

	for i in newList:
		if((i == "ft") or (i == "ft.")):
			newString += i + " "
		else:
			newString += i.capitalize() + " "

	return newString.strip()


# RETURN RANDOM STRING
def getRandomString():
	abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	retString = ""

	now = str(time.time()).split(".")

	for i in range(2):
		rand = random.randrange(0, len(abc))
		retString += abc[rand]

	retString += now[0]
	return retString










lenArg = len(sys.argv)

mp3Retrived = ''

if lenArg >= 2:
	linkYT = sys.argv[1]
	#mp3Retrive = downloadSong(linkYT)
else:
	print("No URL provided")




if __name__ == '__main__':
	app.run(debug=True,host='127.0.0.1',port=5002)














