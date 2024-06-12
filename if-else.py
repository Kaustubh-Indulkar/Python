
player=input("Enter Your Age: ")

if int(player)>=18:
    print("You can vote!!")
elif int(player)<18 and int(player)>5:
    print("You are not eligible")
else:
    print("You are a kid!")        

