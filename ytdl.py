from pytube import YouTube
import pytube
from youtubesearchpython import Search
import os
import json

from db import fetchYTSearchResult,ytSearchResultName


#f = open("test.txt", 'r') #read the file containing tracks (format : trackArtist - trackTitle)
#test_array = f.readlines()
#f.close()

defaultPath = pytube.helpers.target_directory()+'\dl'  #appends the folder path called dl to current working directory
newPath = pytube.helpers.target_directory(defaultPath) #sets this as the new path and creates the folder

#allSearch = Search(test_array[2], limit = 1)
#print(allSearch.result()["result"][0]) #all video information
#print(allSearch.result()["result"][0]["title"]) #video title
#print(allSearch.result()["result"][0]) #video url
#allSearch = Search(test_array[2], limit = 1)
#data = allSearch.result()
#data2 = allSearch.result()["result"][0]["thumbnails"]
#s = json.dumps(data2, indent=2)
#print(s)


#searches a song and returns the url of the top result
def ytSearchResultURL(searchStr): 
    allSearch = Search(searchStr, limit = 1)
    url = allSearch.result()["result"][0]["link"]
    urlString = "\'"+url+"\'" #string of url surrounded by ' '
    return urlString


def ytSearchResultTitle(searchStr): 
    allSearch = Search(searchStr, limit = 1)
    title = allSearch.result()["result"][0]["title"]
    titleStr = "\'"+title+"\'" #string of url surrounded by ' '
    return title

#x = ytSearchResultTitle('babushka boi')
#print(x)

def download(urlString):
    name = YouTube(urlString).title
    rename = name + '.mp3'
    YouTube(urlString).streams.first().download(output_path = newPath, filename=rename)


#returns duration of youtube video in ms (input parameter as url of video)
def duration(urlString):
    duration = YouTube(urlString).length
    return duration * 1000 

#writePlaylist()

#for line in test_array:
    #track = line.rstrip() #each line represents a track (track artist - track title)
    #trackURL = ytSearchResultURL(track)
    #print(track +" *** "+ trackURL + "***" + str(duration(trackURL)))
    #download(trackURL)


def YtSearchStrResult():
    rows = fetchYTSearchResult()

    #print(rows)
    #print(rows[0])

    for row in rows:
            #print(row)
        #print(row[0])
        data2a = ytSearchResultTitle(row[0])
        data2b = ytSearchResultURL(row[0])
        data2c = str(duration(data2b))
        ytSearchResultName(data2a,data2b,data2c,row[0])


YtSearchStrResult() 
