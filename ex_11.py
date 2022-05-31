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
data = 'From stephen.marquard@uct.ac.za /sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
suppos = data.find('')
print(suppos)






