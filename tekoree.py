import tekore as tk

client_id = "6ef640137c4d4b28b09daceed58a8de7"
#print(type(client_id))
client_secret = "1c5b4bd5869f455e9d1e9100e2523673"

app_token = tk.request_client_token(client_id, client_secret)

spotify = tk.Spotify(app_token)

##https://open.spotify.com/playlist/1xHUyPTQsaiuiFspOIQsp7?si=97fe2f36ac4e4481
## https://open.spotify.com/playlist/10gXEiITeD7ISBxqsAruOT?si=44afd709ec484fd8s
#https://open.spotify.com/playlist/5sODFkX36excSGUCvY8Sq9?si=22d0ba50ecb149d2
#sp = spotify.playlist('1xHUyPTQsaiuiFspOIQsp7?si=97fe2f36ac4e4481')
sp = spotify.playlist('10gXEiITeD7ISBxqsAruOT?si=44afd709ec484fd8s')
#sp = spotify.playlist('5sODFkX36excSGUCvY8Sq9?si=22d0ba50ecb149d2') #test track

txt = open('test.txt','a+')
txt_lines = txt.readlines()


##print(sp)

for tracks in sp.tracks.items:
        #print(tracks.track.artists[0].name +" - "+ tracks.track.name) #+" - "+ tracks.track.album.id)
        #print(tracks.track.artists[0].name)
        #print(tracks.track.artists[1].name)
        trackArtist = str(tracks.track.artists[0].name)
        trackName = str(tracks.track.name)
        #print(trackName)

        write_Artist_TrackName = str(trackArtist+" - "+trackName+"\n")
        print(write_Artist_TrackName)
        #txt.write(write_Artist_TrackName)

        #txt.write(trackArtist+" - "+trackName+"\n")


        #for names in tracks.track.artists:
        #print(names.name)
        #print(len(tracks.track.artists[1].name))
        #print(tracks.track.artists[0].name)
        #print(tracks.track.external_ids)
        #print(tracks.track.artists[0].name) #prints artist names

#print(sp.type)

def writePlaylist():
    for tracks in sp.tracks.items:
        trackArtist = str(tracks.track.artists[0].name)
        trackName = str(tracks.track.name)
        write_Artist_TrackName = str(trackArtist+" - "+trackName+"\n")
        txt.write(write_Artist_TrackName)

writePlaylist()
txt.close()