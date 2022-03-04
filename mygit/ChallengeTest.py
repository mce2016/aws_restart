
# Python program to display all the prime numbers within an interval
a_file = open("Prime1.txt", "w")
text = "num, + Prime numbers between 1 and 250 are:"

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
           print("Prime numbers between 1 and 250 are:", num, file=a_file)
           