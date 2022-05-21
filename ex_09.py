#dictionaries

""" purse = dict()
purse['Money'] = 12
purse['Candy'] = 3
purse['food'] = 75
print(purse)
print(purse['Candy'])
purse['Candy'] = purse['Candy'] + 2
print(purse) """

""" lst = list()
lst.append(21)
lst.append(183)
print(lst)
lst[0]=23
print(lst[0])
print(lst)

add =dict()
add['age'] = 23
add['course'] = 180
print(add)
add['age'] = 20
print(add) """

""" dict = {'Fri': 20, 'Thu': 6, 'Sat': 1}
dict['Thu'] = 13
dict['Sat'] = 2
dict['Sun'] = 9
print(dict) """
#--------- dictionaries: common application-------


""" counts = dict()
names = ['cha', 'che', 'cho', 'chan']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts) """

""" counts = {'quincy': 1, 'murgest': 42, 'beau': 1}
print(counts.get('kris', 0)) """
#------Dictionaries and loops---------

""" counts = dict()
print('Enter a line of text:')
line = input('')
words = line.split()
print('Words:', words)
print('Counting...')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts) """

""" counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    if counts[key] > 10:
        print(key, counts[key]) """
#--------------Ex and finiushed --------------------

