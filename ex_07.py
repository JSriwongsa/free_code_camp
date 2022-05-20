#reading files
""" stuff ='Hello\nMuay!'
print(stuff)

xfile = open('ex_02.py')
count = 0
# for line in xfile:
    #print(line)
for line in xfile:
    count = count + 1
print('Line count', count) """

pfile = input('Enter the file name:')
try:
    p1file = open(pfile)
except:
    print('File cannot be opened:', pfile)
    quit()
count = 0
for line in p1file:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, ' subject line in', pfile)  


