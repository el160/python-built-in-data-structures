my_list = [10, 20, 30, 40]
#inserting 15 at the second index

my_list.insert(2,15)

print(my_list)

#extending with another list
list2 = [50, 60, 70]

my_list.extend(list2)
print(my_list)

#remove the last element from the list
my_list.pop()
print(my_list)

#sorting the list in ascending order
my_list.sort()
print(my_list)

#finding and printing the index value of 30 in list
print(my_list.index(30))