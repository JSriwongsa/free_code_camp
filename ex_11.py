#----- Regular expressions -----
hand = open('mbox-short.txt')
for line in hand:
    line =line.rstrip()
    #if line.find('From:') >= 0:
    if re.search('from:', line):
        print(line)
# ----- RegEx B -----




