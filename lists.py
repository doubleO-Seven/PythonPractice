friends = ["ironMan", "Thor", "Wanda"]
print(friends)


friends = ["ironMan", "Thor", "Wanda"]
print(friends[0])

friends = ["ironMan", "Thor", "Wanda"]
print(friends[-1])

# starting print from nth index
friends = ["ironMan", "Thor", "Wanda", "Falcon"]
print(friends[2:])

#replace with another 

friends = ["ironMan", "Thor", "Wanda"]
friends[2] = "SpideMan"
print(friends)

#sort the list

friends = [10, 25, 62, 2, 5]
friends.sort()
print(friends)

# print all item in the list

for x in friends:
    print(x)

# a mumber is in out of the list

if 10 in friends:
    print("Yes")
else:
    print("No") 

print(len(friends))

# insert last

friends.append(2333)
print(friends)

# insert in a specific position

friends.insert(2, 555)
print(friends)

# remove an item

item = friends.remove(10)
print(friends)

# delete all 
'''
item = friends.clear()
print(friends) '''

# reverse

list = friends.reverse()
print(friends)

# new list with nth same variables 
mylist = [0] * 10
print(mylist)

# adding two list 

mylist2 = [1,2,3,4,5,6,7]
new = mylist + mylist2
print(new)