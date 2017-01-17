
def fizz_buzz(n):
    for num in range(1,n): #identify a number between 1 and n

        if num%3==0 and num%5==0: # Checking for dividiblity by 3 and 5
	        return ("FizzBuzz")

        elif num%3==0:
	        return("Fizz")

        elif num%5==0:
	        return("Buzz")

        else:
	        return(n)

if __name__=="__fizz_buzz__":fizz_buzz()
