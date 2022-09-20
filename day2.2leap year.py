n=float(input('enter the value:'))
if(n>0 and n is integer()):
    if(n%4==0 or n%400==0):
        print ('it is a leap year')
    else:
        print ('it is not a leap year')
        if n%4!=0:
            n-=int(n%4)
            print(n," leap year")
else:
    print ('not a valid year')
