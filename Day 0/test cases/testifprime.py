#Test Analysis
#testing if the values obtained are prime numbers


num=int(input("Input a number"))

if num>1:
    for p in range(1,num):
        if (num % p)==0:
            print(num,"IS NOT a Prime number")
            break
            
    else:
        print(num, "IS a Prime Number")

else:
    print(num,"IS NOT a prime number")
