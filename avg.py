# Find min and max of given numbers

lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("Maximum element in the list is :", max(lst), "\nMinimum element in the list is :", min(lst))

# Find Sum and Average of N Natural Numbers
 
number = int(input("Please Enter any Number: "))
total = 0

for value in range(1, number + 1):
    total = total + value

average = total / number

print("The Sum of Natural Numbers from 1 to {0} =  {1}".format(number, total))
print("Average of Natural Numbers from 1 to {0} =  {1}".format(number, average))
