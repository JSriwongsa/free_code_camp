#!/usr/bin/env python3

""" import urllib.request, urllib.parse, urllib.error

from numpy import True_
import twurl
import json

twitter_url = 'https://api.twitter.com/1.1/friends/list.json'

while True_:
    print('')
    acct = input('Enter Twitter account:')
    if (len(acct) < 1) : break
    url = twurl.augment(TWITTER_URL, {'screen_name' :acct, 'count': '5'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url)
    data = connection.read() .decode()
    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])
    js = json.loads(data)
    print(json.dumps(js, indent=4))

    for u in js['users']:
        print(u['screen_name'])
        s = u['status']['text']
        print(' ', s[:50]) """    #--- request for the key ---

 #----- Exercise_geojason in code3 -----
 #----- Exercise_json in code3(json1&json2) -----






