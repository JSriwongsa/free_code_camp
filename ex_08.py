#lists

""" fruit = 'banana'
x = fruit[1]
print(x) """
#---------- Concatenating list using + ------

""" a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
t = [9, 41, 12, 3, 74, 15]
print(t[:3])

stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)

friends = ['John', 'Emily', 'Sally']
friends.sort()
print(friends)
print(friends[1]) """
#------ Split function ------

""" a = 'With three words'
stuff = a.split()
print(stuff)
print(len(stuff))
print(stuff[0])
for w in stuff:
    print(w) """

""" fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    print(words[2]) """
    
""" words = 'His e-mail is q-lar@freecodecamp.org'
pieces = words.split()
parts = pieces[3].split('-')
n = parts[1]
print(n) """

han = open('mbox-short.txt')
for line in han:
    line = line.rstrip()
    #print('Line:', line)
    if line == '':
        print('Skip Blank')
        continue
    words = line.split()
    print('Words:', words)
    #guardian
    """ if len(words) <1:
        continue """
    if words[0] != 'From' :
        #print('Ignore')
        continue
    print(words[2])










