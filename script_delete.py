import soundcloud
from bs4 import BeautifulSoup
import requests
import urllib
import json
import os

client = soundcloud.Client(client_id='',
                           client_secret='',
                           username='',
                           password='')

# upload audio file
tracks = client.get('/me/tracks')


for track in tracks:
    uploaded = None
    with open('dialogs.json', 'a+') as outfile:
        try:
            uploaded = json.load(outfile)
        except ValueError:
            uploaded = []
        print uploaded
    if any(track.uri in s['url'] for s in uploaded):
        print "--> " + track.uri + " already uploaded"
        continue
    print track.title
    client.delete("/tracks/" + str(track.id))
