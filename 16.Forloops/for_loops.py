#for loops
for item in 'I love python':
    print(item)

for item in range(1,10):
    print (item)

#Sample Exercise
#script to calculate the  cost of all the items in a shopping cart.
# prices = 10, 120, 30.
prices = [10,20,30]
total = 0
for item in prices:
    total += item
print(total)