hour = input('Enter your hour')
rate = input('Enter your rate')
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

