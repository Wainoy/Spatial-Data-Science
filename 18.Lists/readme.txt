The scripts contain sample exercises on lists. 
A list is a collection of items
lists are defined using square brackets []
Lists are ordered and indexed form zero [0]
 
it is a continuation of the exercise on lists
2D_Lists.py explains about 2D lits
List_Methods.py explains about list methods and functions: 
	adding items to a list append()
	remove items from a list remove()
	sort items in a list or reverse order sort() and reverse()
	check for the occurrence of an item in a list using 'in' or index()
	check the frequency of occurrence of an object: count() etc
	make a copy of a list using the copy() method

#exercise
#program to remove duplicate items from a list
numbers = [1,2,3,5,5,7,10,11,3,1,5]
uniques = []
for number in numbers:
   if number not in uniques:
       uniques.append(number)
print(uniques)