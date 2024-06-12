first=input("Enter First Number: ")
operator=input("Select the Operation you want(+,-,*,/): ")
second=input("Enter Second Number: ")

first=int(first)
second=int(second)

if operator=="+":
    print(first+second)
elif operator=="-":
    print(first-second)    
elif operator=="*":
    print(first*second)  
elif operator=="/":
    print(first/second)   
else:
    print("Invalid Number")           

#Range

number=range(5)
print(number)