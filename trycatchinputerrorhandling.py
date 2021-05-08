print('How many cats do you have')
num=input()
try:
    if int(num) >= 4:
        print('you have lot of cats')
    else:
        print('you do not have lot many cats')
except:
    print('Input is not a number')
