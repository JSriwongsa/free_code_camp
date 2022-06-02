#!/usr/bin/env python3

#----- networked programs -----
""" import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))  """ #---- host + port ------

#----- networking protocol & write a web browser-----

""" import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
mysock.close() """

# ----- Using urllib ----- it is shorter than using socket

import urllib.request
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

counts = dict()
for line in fhand:
    words = line.decoide().split()
    for word in words:
        counts[word] = counts.get(word, 0) +1
print(counts)






