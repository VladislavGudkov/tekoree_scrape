from qbittorrent import Client

import json

qb = Client('http://127.0.0.1:8686/')

qb.login
torrents = qb.torrents()



for torrent in torrents:
    print (torrent['name'])


s = json.dumps(torrent, indent=2)
print(s)

   