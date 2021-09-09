import tekore as tk
import sqlite3
from db import writeDB


client_id = "6ef640137c4d4b28b09daceed58a8de7"
client_secret = "1c5b4bd5869f455e9d1e9100e2523673"
app_token = tk.request_client_token(client_id, client_secret)
spotify = tk.Spotify(app_token)

#sp = spotify.playlist('10gXEiITeD7ISBxqsAruOT?si=44afd709ec484fd8s') #https://open.spotify.com/playlist/10gXEiITeD7ISBxqsAruOT?si=44afd709ec484fd8s
#sp = spotify.playlist('4LOBV27lxnbuE0Hgu31gG6?si=7f3725f7fa2540cd') #https://open.spotify.com/playlist/4LOBV27lxnbuE0Hgu31gG6?si=7f3725f7fa2540cd
#sp = spotify.playlist('1BuO4i8QX9ABB7GGUZmOje?si=adcdc628d78b49c7') #https://open.spotify.com/playlist/1BuO4i8QX9ABB7GGUZmOje?si=adcdc628d78b49c7 
sp = spotify.playlist('3TEjeoqVNi6aE2KJE1qlP4?si=fc6723e9d6864e70') #https://open.spotify.com/playlist/3TEjeoqVNi6aE2KJE1qlP4?si=fc6723e9d6864e70

sp1 = spotify.track('7qP3rBLJkXHff4YwVLhJ0i?si=3dd30f811e83497e')
sp2 = spotify.track_audio_analysis('7qP3rBLJkXHff4YwVLhJ0i?si=3dd30f811e83497e')
sp3 = spotify.track_audio_features('7qP3rBLJkXHff4YwVLhJ0i?si=3dd30f811e83497e')

def populateSpotify():

    for tracks in sp.tracks.items:
        
            trackArtists = []

            trackName = str(tracks.track.name) 
            trackArtist = str(tracks.track.artists[0].name) #alias of album artist in windows
            trackAlbum = tracks.track.album.name 
            trackDiscNumber = tracks.track.disc_number #track disc number 
            trackNumber = tracks.track.track_number #track number in its album
            trackDurationMS = tracks.track.duration_ms #track duration in milliseconds
            trackISRC = tracks.track.external_ids['isrc'] #track ISRC code for comparisons
            trackID = tracks.track.id #track id for spotify
            trackURL = tracks.track.external_urls['spotify'] #track url to spotify player in web
            trackPopularity = tracks.track.popularity  #track popularity 

            for artist in tracks.track.artists:
                artistName = artist.name
                trackArtists.append(artistName)
        
            otherTrackArtists = trackArtists[1:]  #alias of contributing artists in windows
            strOtherTrackArtists = str(otherTrackArtists)[1:-1].replace("'","")
            #print(strOtherTrackArtists)     
            writeDB(trackName,trackArtist,strOtherTrackArtists,trackDiscNumber,trackNumber,trackDurationMS,trackISRC,trackID,trackURL)


populateSpotify()




def writePlaylist():
    for tracks in sp.tracks.items:
        trackArtist = str(tracks.track.artists[0].name)
        trackName = str(tracks.track.name)
        write_Artist_TrackName = str(trackArtist+" - "+trackName+"\n")
        txt.write(write_Artist_TrackName)

#txt = open('test.txt','a+')
#writePlaylist()
#txt.close()




