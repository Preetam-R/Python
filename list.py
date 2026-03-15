# Lists
# A list is a built-in data structure in Python, used to store multiple elements.
# Lists are used by many algorithms.

# Create Algorithms
# Sometimes we want to perform actions that are not built into Python.
# Then we can create our own algorithms.
#---------------------------------------------------------------------------------------------------#
# Example
# Create an algorithm to find the lowest value in a list:

#we can take both user input or declare a list

#declaring the list
lst = [9,5,2,7,8,1]
minval = lst[0]

for i in lst:
    if i < minval:
        minval = i

print(f"the lowest number in the list is {minval}")