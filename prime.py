# Python program to display all the prime numbers within an interval

# change the values of a and b for a different result
a = 100
b = 500

print("Prime numbers between",a,"and",b,"are:")

for num in range(a,b + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
