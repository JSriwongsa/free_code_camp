#Looping through strings

""" for n in 'banana':
    print(n)

fruit = 'banana'
x = len(fruit)
print(x)

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count) """

word = 'bananana'
i = word.find('na')
print(i)

str = 'X-DSPAM-Confidence: 0.8475'
a = str.find(':')
print(a)
b = str[a+1:]
print(b)
value = float(b)
print(value)

