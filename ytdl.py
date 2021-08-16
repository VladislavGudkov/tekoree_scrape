from pytube import YouTube
import pytube
from youtubesearchpython import Search
import os

f = open("test.txt", 'r')
test_array = []
test_array = f.readlines()
#print(test_array)
#print(f.readlines())



allSearch = Search(test_array[2], limit = 1)
#print(allSearch.result()["result"][0])
print(allSearch.result()["result"][0]["title"])
print(allSearch.result()["result"][0]["link"])

title = allSearch.result()["result"][0]["title"]

url = allSearch.result()["result"][0]["link"]
urlString = "\'"+str(url)+"\'"
print(urlString)


#for lines in f.readlines():
    #print(lines.rstrip())

#name = pytube.extract.video_id(url)


def download(urlString):
    name = YouTube(urlString).title
    rename = name + '.mp3'
    YouTube(urlString).streams.first().download(filename=rename)



#download(urlString)