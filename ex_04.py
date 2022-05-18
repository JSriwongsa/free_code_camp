#learn about using function 'def'

""" big = max('Hello sunshine') #the item with the highest value in an iterable.
print(big) """               #-----the result show 'u' -----

""" num = max(2, 3, 5, 9)
print(num) """               #----- the result shows '9' -----
#-----------------------------------------------
""" x=10
print('Hello')

def print_word():
    print('I am a graduate student')
    print('I am interested in Physics')

print('there')
#print_word()
x = x + 10
print(x) """
#--------------------------------

""" def greet():
    return'Hello'
print(greet(), 'Juthatip')
print(greet(), 'Sriwongsa') """
#----------------------------------

""" def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else :
        return 'Hello'

print(greet('en'), 'Toro')
print(greet('es'), 'Molly')
print(greet('fr'), 'Minnie') """
#-----------------------------------
""" def fred():
    print('Zap')
def jane():
    print('ABC')

jane()
fred()
jane()  """              #---- the result shows === ABC Zap ABC -------
#------------------------------------

def computepay(hours, rate):
    #print('In computepay', hours, rate)
    if hours > 45:
   # print('Overtime')
        reg = hours * rate
        otp = (hours - 45) * (rate * 0.5)
    #print(reg, otp)
        pay = reg + otp 
    else : 
   # print('Regular')
        pay = hours * rate
    #print('Returning', pay)
    return pay

hours = input('Enter your hours:')
rate = input('Enter your rate:')

""" try:
    int(hours)
    int(rate)
except:
    print('Error, please enter a number')
    quit()

pay = int(hours) * int(rate) 
print('Pay:', pay) """

computepay(int(hours), int(rate))
pay1 = computepay(int(hours), int(rate))

""" if int(hours) > 45:
   # print('Overtime')
    reg = int(hours) * int(rate)
    otp = (int(hours) - 45) * (int(rate)*0.5)
    #print(reg, otp)
    pay = reg + otp 
else : 
   # print('Regular')
   pay = int(hours) * int(rate) """
print('Pay:', pay1)

