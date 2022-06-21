x = int(input("enter a number x: "))

if(x<100):
    if(x%2==0):
        print("number is even")
    else:
        print("number is odd")
elif(x==100):
    print("number is equal to 100")
else:
    print("number is greater than 100")
