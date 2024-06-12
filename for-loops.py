for i in range(10):
    print(i)

#List

marks=[97,90,100,"english"]
print(marks)   

marks=[97,90,100,"english"]
print(marks[1]) 
print(marks[-1]) 
print(marks[1:4]) 


#for loop in Lists
for score in marks:
   print(score)
 
marks.append(100)#-->to add number at last
print(marks) 

marks.insert(1,35)#--->to add number on the index you want
print(marks)

print("english" in marks)#-->to search element

print(marks)#--->6
print(len(marks))#--->to check length

z=0
while z<len(marks):
    print(marks[z])
    z=z+1

marks.clear()
print(marks)    