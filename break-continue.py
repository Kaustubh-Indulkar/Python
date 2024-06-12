players=["ronaldo","de gea","messi","musiala","walker"]

for palyers in players:
    if palyers=="messi":
        break;
    print (palyers)

for player in players:
    if player=="musiala":
        continue;
    print (player) 


#tuple

marks=(67,50,89,69,69)

#can perform 2 operations count & index
print(marks.count(69))
print(marks.index(50))

#sets-->to keep unique elements

goals={130,108,103,98}

for goal in goals:
    print(goal)

#dictionary

goalll={"ronaldo":130,"messi":103}    

print(goalll["ronaldo"])
print(goalll["messi"])

goalll["chhetri"]=98;
print(goalll)

goalll["chhetri"]=99;
print(goalll)


