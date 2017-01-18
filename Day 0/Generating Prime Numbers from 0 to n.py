lower = 0
n = int(input("Enter upper range: "))

print("Prime numbers between",lower,"and",n,"are:")

for num in range(lower,n + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
