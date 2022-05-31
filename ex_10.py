#----- Tuples------

""" x = ('Glenn', 'Sally', 'Joshep' )
print(x[2])
y = (1, 2, 9)
print(y)
print(max(y))
for iter in y:
    print(iter)

d = dict()
d['quincy'] = 1
d['beau'] = 5
d['kris'] = 9
for (k,i) in d.items():
    print(k, i) """

#-----sorting lists of tuples-----

fname = input("Enter the Filename: ")
if len(fname) < 2:
  fname = "clown.txt"

try:
  fhand = open(fname,"r")
except:
  print("Invalid Filename.Try again!")
  quit()

d = dict()
for line in fhand:
  line = line.rstrip()
  words = line.split()

  for word in words:
    d[word] = d.get(word,0)+1

common = sorted([(v,k) for k,v in d.items()],reverse=True)
print(common[:5])