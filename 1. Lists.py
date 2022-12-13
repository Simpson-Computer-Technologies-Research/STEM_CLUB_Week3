# /////////////////
# //    Lists    //
# /////////////////

# // You can have any type of variable in a python list
list_1 = ["hey", 0, 1.0]

# // Lists are indexed by 0, 1, 2, ... not 1, 2, 3, ...
list_2 = [1, 2, 3]

print(list_1)
print(list_2)

# // Accessing Lists
list_1_value = list_1[0]
list_2_value = list_2[2]

print(list_1_value)
print(list_2_value)

# // Setting specific index in a list
list_1[1] = "new item"

print(list_1)

# // Adding an item to a list
list_1.append("new item")

print(list_1)

# // Removing an item from a list
del list_1[0]

print(list_2)

# // Get length of a list
list_1_length = len(list_1)

# // Print values in a list using a ranged for loop
for i in range(list_1_length):
  print(list_1[i])
