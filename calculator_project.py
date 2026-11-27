num1=int(input("Enter the num1= "))
num2=int(input("Enter the num2= "))
op=input("enter the any operators +,-,*,**,/,//,%= ")
if op=="+":
    result= num1+num2
    print(result)
elif op=="-":
    result= num1-num2 
    print(result)
elif op=="*":
    result= num1*num2
    print(result)
elif op=="**":
    result=num1**num2
    print(result)
elif op=="/":
    result= num1/num2
    print(result)
elif op=="//":
    result= num1//num2
    print(result)
elif op=="%":
    result= num1%num2
    print(result)
else:
    print("Unvalid opreator, please try again")                    
