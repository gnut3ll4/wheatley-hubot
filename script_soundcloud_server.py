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

url = "http://theportalwiki.com/wiki/Wheatley_voice_lines/fr"

headers = {
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

for link in soup.find_all("a",{ "class":"internal" }):
    file_url = link.get('href')
    file_name = file_url.rsplit('/', 1)[-1]
    uploaded = None

    with open('dialogs.json', 'a+') as outfile:
        try:
            uploaded = json.load(outfile)
        except ValueError:
            uploaded = []
        # uploaded = outfile.read().splitlines()
        print uploaded
        # continue
    if any(file_name in s['title'] for s in uploaded):
        print "--> " + file_name + " already uploaded"
        continue

    dialog = link.string

    urllib.urlretrieve (file_url, file_name)

    # upload audio file
    track = client.post('/tracks', track={
        'title': file_name,
        'asset_data': open(file_name, 'rb')
    })

    print file_name
    print track.id

    # fetch a track by it's ID
    track = client.get('/tracks/' + `track.id`)

    # update the track's metadata
    client.put(track.uri, track={
      'description': dialog,
      'genre': 'None',
      'artwork_data': open('wheatley.jpg', 'rb')
    })

    os.remove(file_name)
    wheatley_voice = {"title":file_name, "url":track.uri, "dialog":dialog}
    with open('dialogs.json', 'w') as outfile:
        uploaded.append(wheatley_voice)
        json.dump(uploaded, outfile)
    # with open('uploaded.txt', 'a+') as outfile:
    #     outfile.write(file_name + '\n')

# json_data = json.dumps(json_data)

# with open('dialogs.json', 'w+') as outfile:
#     json.dump(json_data, outfile)
