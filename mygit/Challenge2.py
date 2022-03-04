"""
Your module description
"""
# Python program to display all the prime numbers within an interval
a_file = open("Prime.txt", "w")
text = "num"

lower = 1
upper = 250

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num, file=a_file)
           