#continuation of lists
names = ['Jane', 'John', 'Jean', 'James', 'Sean']
print(names[:]) #prints all the names
print(names[:-1]) #prints all the names except 'Sean'
print(names[2:]) #prints names from 'Jean' to 'Sean'
names[4] = 'Eve' #change item at index 4
print(names)
names.append('Moses') # append() is a method that adds a single item to the list
print(names)
more_names = 'April', 'June', 'Mary'
print(more_names)
print(type(more_names))
names.extend(more_names) #how to use the extend() function to add more names. the function also takes one argument only.
print(names)
