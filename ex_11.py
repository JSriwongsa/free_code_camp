#!/usr/bin/env python3

#----- Regular expressions -----
""" hand = open('mbox-short.txt')
for line in hand:
    line =line.rstrip()
    if line.find('From:') >= 0:
        print(line) """

# ----- RegEx B -----

""" import re
x = 'My two favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y) """

""" import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s) 
print(lst) """

#------ string parsing examples -----
#data = 'From stephen.marquard@uct.ac.za /sat Jan 5 09:14:16 2008'
""" atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos+1 : sppos]
print(host) """  #----- a bit annoying to remember lol -------

""" line = data
words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])

import re
line = data
y = re.findall('@([^ ]*)', line)  #--- [^] = non blank character---
print(y) """

import re
hand = open('mbox.txt')
numlist = list
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidemce: ([0-9.]+)', line)
    if len(stuff) != 1 : continue
    num = float(stuff([0]))
    numlist.append(num)
print('Maximum:', max(numlist))


""" x = ' we just got $10.00 for cookies'      #----- run w/ import re -----
y = re.findall('\$[0-9.]+', x)
print(y) """










