a=input ("Enter the month:")
b=int (input("Enter the date:"))

if(b>0):

    if(a=='Mar' or a=='Apr' or a=='May'):
       if (b>=20):
           print("The season is currently summer")
       else:
           print ("The seasonis currently winter")
    elif (a=='Jun' or a =='Jul' or a=="Aug"):
        if(b>=21):
            print("The season is currently spring")
        else:
            print("The seasonia currently summer")
    elif (a=='Sep' or a =='Oct' or a =='Nov'):
        if(b>=22):
            print("The season is currently fall")
        else:
            print ("The seasonis currently spring")
    elif (a==' Dec' or a==' Jan' or a=='Feb'):
        if(b>=21):
            print("The season is currently winter")
        else:
            print("The seasonis currently fall")
    else:
        print("Enter valid three letters of month")
else:
    print("The given date is invalid")
