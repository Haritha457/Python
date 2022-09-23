
a=input("Enter the grade of the employee:")
try:
    b=int(input("Enter the employee salary:"))
    if(b>0):
        if(a=='A'):
            if(b<10000):
                c=b*7/100
                print("Salary:",b)
                print("Bonus:",c)
                print("Total to be paid:",b+c)
            else:
                c=b*5/100
                print("Salary:",b)
                print("Bonus:",c)
                print("Total to be paid:",b+c)
        elif(a=='B'):
            if(b<10000):
                c=b*12/100
                print("Salary:",b)
                print("Bonus:",c)
                print("Total to be paid:",b+c)
            else:
                c=b*10/100
                print("Salary:",b)
                print("Bonus:",c)
                print("Total to be paid:",b+c)
        else:
            print("INVALID GRADE")
    elif(b==0):
        print("Salary cant be in zero")
    else:
        print("Salary cant be in negative")
except ValueError:
    print("INVALID INPUT")
