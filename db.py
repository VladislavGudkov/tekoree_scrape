import sqlite3
from sqlite3 import Error

#from ytdl import ytSearchResultTitle

conn = sqlite3.connect('music.db')
c = conn.cursor()

    


def createSpotifyTable():
    conn = sqlite3.connect('music.db')
    c = conn.cursor()
    create_table_spotify = '''CREATE TABLE IF NOT EXISTS spotify
              (trackName TEXT NOT NULL, 
              trackArtist TEXT NOT NULL, 
              otherTrackArtists TEXT, 
              trackDiscNumber INT, 
              trackNumber INT, 
              trackDurationMS INT, 
              trackISRC TEXT, 
              trackID TEXT, 
              trackURL TEXT,
              PRIMARY KEY (trackName))
              '''
    c.execute(create_table_spotify)
    conn.commit()
    c.close()

def dropSpotifyTable():
    conn = sqlite3.connect('music.db')
    c = conn.cursor()
    command = '''DROP TABLE IF EXISTS spotify'''
    c.execute(command)
    conn.commit()
    c.close()

def createYoutubeTable():
    conn = sqlite3.connect('music.db')
    c = conn.cursor()
    create_table_yt = '''CREATE TABLE IF NOT EXISTS Yt
              (trackName TEXT REFERENCES spotify (trackName), 
              trackArtist TEXT NOT NULL, 
              ytTrackSearchStr TEXT,
              ytSearchResultName TEXT,
              ytTrackURL TEXT,
              ytTrackDurationMS INT 
              )
              '''
    c.execute(create_table_yt)
    conn.commit()
    c.close()

def dropYoutubeTable():
    conn = sqlite3.connect('music.db')
    c = conn.cursor()
    command = '''DROP TABLE IF EXISTS Yt'''
    c.execute(command)
    conn.commit()
    c.close()

def writeDB(trackName,trackArtist,otherTrackArtists,trackDiscNumber,trackNumber,trackDurationMS,trackISRC,trackID,trackURL):
    conn = sqlite3.connect('music.db')
    c = conn.cursor()
    data_tuple = (trackName,trackArtist,otherTrackArtists,trackDiscNumber,trackNumber,trackDurationMS,trackISRC,trackID,trackURL)

    spotify_insert_query = '''INSERT INTO spotify
              (trackName,trackArtist,otherTrackArtists,trackDiscNumber,trackNumber,trackDurationMS,trackISRC,trackID,trackURL)
              VALUES
              (?,?,?,?,?,?,?,?,?);
              '''
    c.execute(spotify_insert_query,data_tuple)
    conn.commit()
    c.close()

def fetchSpTrackArtist(trackArtist):
    conn = sqlite3.connect('music.db')
    c = conn.cursor()
    select = '''SELECT trackArtist FROM spotify WHERE trackArtist = ?'''
    c.execute(select,(trackArtist,))
    rows = c.fetchone()
    return rows[0]
    
def fetchSpTrackName(trackName):
    conn = sqlite3.connect('music.db')
    c = conn.cursor()
    select = '''SELECT trackName FROM spotify WHERE trackName = ?'''
    c.execute(select,(trackName,))
    rows = c.fetchone()
    return rows[0]


def fetchYTSearchResult():
    conn = sqlite3.connect('music.db')
    c = conn.cursor()
    select = '''SELECT ytTrackSearchStr FROM Yt'''
    c.execute(select)
    rows = c.fetchall()
    conn.close()
    return rows
    

#fetch function to grab database
def fetchSpRows():
    conn = sqlite3.connect('music.db')
    c = conn.cursor()
    select = '''SELECT * FROM spotify'''
    c.execute(select)
    rows = c.fetchall()
    conn.close()
    return rows

def fetchYtRows():
    conn = sqlite3.connect('music.db')
    c = conn.cursor()
    select = '''SELECT * FROM Yt'''
    c.execute(select)
    rows = c.fetchall()
    conn.close()
    return rows

def writeYT():
    conn = sqlite3.connect('music.db')
    c = conn.cursor()
    #insert = '''INSERT INTO Yt (trackName,trackArtist,ytTrackSearchStr,ytSearchResultName,ytTrackDurationMS,ytTrackURL) VALUES (?,?,?,?,?,?);'''
    #c.execute(spotify_insert_query,data_tuple)
    ins = '''INSERT INTO  Yt(trackName, trackArtist) SELECT trackName, trackArtist from spotify'''
    c.execute(ins)
    conn.commit()
    c.close()

def YTSearch():
    rows = fetchYtRows()

    conn = sqlite3.connect('music.db')
    #print(rows)

    for row in rows:
        #update = '''UPDATE Yt SET ytTrackSearchStr = ?'''
        test = '''UPDATE Yt set ytTrackSearchStr = trackArtist || ' - ' || trackName;'''
        print(row)
        c = conn.cursor()  
        c.execute(test)
        conn.commit()


def ytSearchResultName(ytSearchResultTitle,ytTrackURL,ytTrackDurationMS,ytTrackSearchStr):

    #rows = fetchYTSearchResult()
    conn = sqlite3.connect('music.db')
    c = conn.cursor()
    data_tuple = (ytSearchResultTitle,ytTrackURL,ytTrackDurationMS,ytTrackSearchStr)
    test = '''UPDATE Yt set ytSearchResultName = ?, ytTrackURL = ?, ytTrackDurationMS = ?  WHERE ytTrackSearchStr = ? ;'''
    c.execute(test,data_tuple)
    conn.commit()




#def populateSP():
#dropSpotifyTable()
#createSpotifyTable()
#populateSpotify()


#dropYoutubeTable()
#createYoutubeTable()
#writeYT()
#YTSearch()

