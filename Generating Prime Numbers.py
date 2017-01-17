#"A simple way of getting prime numbers in a given range"
#This is a trial code and seems to give me repeating numbers

n=int(input("Enter a number:"))
print ("Prime numbers within the limit are:")

for num in range(0,n):
    if num > 1:
        for i in range(2,num):
            if (num % i) ==0:
                break
            else:
                print(num)
    
