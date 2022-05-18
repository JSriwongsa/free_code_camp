hour = input('Enter your hours:')
rate = input('Enter your rate:')

try:
    int(hour)
    int(rate)
except:
    print('Error, please enter a number')
    quit()

pay = int(hour) * int(rate) 
print('Pay:', pay)

if int(hour) > 45:
    print('Overtime')
    reg = int(hour) * int(rate)
    otp = (int(hour) - 45) * (int(rate)*0.5)
    print(reg, otp)
    pay = reg + otp 
else : 
    print('Regular')

#in case of not typing a numerical number we can put "try and except" to not blow up the program
