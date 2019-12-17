import eyed3
from eyed3.id3 import Tag
from tinytag import TinyTag

audio = eyed3.load("./helloWorld.mp3")

# if(audio.tag == None):
# 	audio.initTag()

# audio.tag.images.set(3, open('music.png','rb').read(), 'image/png')

# audio.tag.title = u"aaa"
# audio.tag.artist = u"bb"
# audio.tag.album_artist = u"bb"

# # audio.tag.genre = u"ccc"
# musicajd = "MusicaJD"
# audio.tag.album = unicode(musicajd)
# audio.tag.genre = u"dd"

# audio.tag.save()

# # print(audio)

# # USE TINY TAG TO GET ATTRIBUTES
# tag = TinyTag.get('./helloWorld.mp3')
# # print('Title %s.' % tag.title)
# # print('Artist %s.' % tag.artist)
# # print('Album Artist %s.' % tag.albumartist)
# print('Genre %s.' % tag.genre)
# print('Album %s.' % tag.album)
# # Image

# print('Disc %s.' % tag.disc)
# print('Year %s.' % tag.year)
# print('Track %s.' % tag.track)
# print('Comment %s.' % tag.comment)


video = "https://www.youtube.com/watch?v=5ytzbr4SiKE"

from urllib import request, parse 
from urllib.parse import parse_qs


parsed = parse.urlparse(video)
video_id = parse_qs(parsed.query)['v'][0]

resp = request.urlopen(video)
data = resp.read()
decode_data = data.decode("UTF-8")

video_title = decode_data.split("</title>")[0].split("<title>")[1].split(" - YouTube")[0]

print(video_id)


print(title1)