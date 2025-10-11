l = [1, 2, "tops", "rahul", 28.4, True, False, "python", 10, 20, 1, 2, "java"]
print(l)
print(len(l))

l1 = l.copy() #use of copy function to copy all data of list in another list
print(l1)
l1.append(200)
print(l1)
print(l)

l2 = l
print(l2)
l2.append(300)
print(l2)
print(l)

print(l.count(1)) #use of count function to count the number of occurence of perticular data in list
# in count true=1 and false=0

l3 = [1000, 2000, 3000]
l.extend(l3) #use of extend function to add multiple data in list in last
print(l)

print(l.index("tops")) #use of index function to find the index of perticular data in list
print(l.index(10))

l.insert(4, "Dhvanit") #use of insert function to add data in list on perticular index
print(l)