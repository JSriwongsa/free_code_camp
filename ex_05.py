#learn about repeated steps

""" n = 5
while n > 0:
    print(n)
    n = n - 1
#print('Blastoff!')
print(n) """
#-----------------------------
""" n = 0
while n >= 0:
    print('Lather')
    print('Rinse')
    #n = n-1
    #print(n)
print('Dry off!') """
#----------------------------
""" n = 0
while True:
    if n == 3:
        break
    print(n)
    n = n + 1 """
#-----------------------------
""" for  i in[5, 4, 3, 2, 1]:
    print(i)
print('Blastoff')



friends = ['A', 'B', 'C', 'D', 'E']
for friend in friends:
    print('Happy New Year 2022:', friend)
#print('Done!') """
#------------------------------
""" print('Before')
for thing in [8, 17, 39, 9, 5, 7]:
    print(thing)
print('After') """
#---------------------------------------
""" largest_so_far = -1
print('Before', largest_so_far)
for the_num in [8, 17, 39, 9, 5, 7]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)

print('After', largest_so_far) """

#-----------------------------------------
""" smallest = None
print('Before:', smallest)
for num in [3, 41, 12, 9, 74, 15]:
    if smallest is None or num < smallest:
        smallest = num
        #break   ------> it causes the loop 'BREAK' 
    print('Loop:', num, smallest)
print('Smallest:', smallest) """
#------------------------------------------
#----- Counting in a loop ------

""" set = 0
print('Before', set)
for thing in [3, 4, 7, 15, 21]:
    set = set + 1
    print(set, thing)
print('After', set) """

""" count = 0
sum = 0
print('Before', count, sum)
for value in [3, 4, 5, 7, 15, 21]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum/count) """

""" found = False
print('Before', found)
for value in [3, 4, 5, 7, 15, 21]:
    if ((value == 3) or (value == 5)):
        found = True
    else :
        found = False
    print(found, value)
print('After', found) """


num = 0
tot = 0.0
while True:
    svalue = input('Enter your number:')
    if svalue == 'done':
        break

    try:
        vvalue = float(svalue)
    except:
        print('Invalid value')
        continue

    #print(vvalue)
    num = num + 1
    tot = tot + vvalue

#print('All done')
print(num, tot, tot/num)








