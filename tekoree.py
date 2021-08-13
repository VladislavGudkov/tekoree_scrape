import tekore as tk

client_id = "client_id_here"
#print(type(client_id))
client_secret = "client_secret_here"

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
        #print(tracks.track.name +" - "+ tracks.track.artists[0].name +" - "+ tracks.track.album.id)
        print(tracks.track.artists[0].name)
        #print(tracks.track.artists[1].name)
        track1 = str(tracks.track.artists[0].name)
        
        #txt.write(track1+"\n")

txt.close()
        #for names in tracks.track.artists:
         #   print(names.name)
        #print(len(tracks.track.artists[1].name))
        #print(tracks.track.artists[0].name)
        #print(tracks.track.external_ids)
        #print(tracks.track.artists[0].name) #prints artist names

#print(sp.type)
