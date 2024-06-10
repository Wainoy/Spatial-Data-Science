list methods
numbers = [1,2,3,4,5,6,7,8,9]
numbers.append(10)
print(numbers)
numbers.insert(0,0)
print(numbers)
numbers.remove(10)
print(numbers)
numbers[2] = 1
print(numbers.count(1)) #return the frequency of 1 in the list
print(numbers.count(11)) #returns 0
print(5 in numbers) #returns true
numbers2 = numbers.copy()
print(numbers2)
numbers.sort()
numbers.reverse()
print(numbers)
#print(numbers.index(55)) #value error : 55 not in the list


#exercise
#program to remove duplicate items from a list
numbers = [1,2,3,5,5,7,10,11,3,1,5]
for number in numbers:
   if numbers.count(number) != 1:
       numbers.remove(number)
print(numbers)
