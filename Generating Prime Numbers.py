#"A simple way of getting prime numbers in a given range"
limit=int(input("Enter the limit:"))

print ("Prime numbers within the limits are:")

for num in range(0,limit):
    if num > 1:
        for i in range(2,num):
            if (num % i) ==0:
                break
            else:
                print(num)
    
