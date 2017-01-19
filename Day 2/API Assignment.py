
import requests     #will import the module called requests

response = requests.get("http://api.open-notify.org/astros.json")
info = response.json() # will request for data from the api 
    # Will give the final output

if response.status_code == 200:
    print("\nWant to play 'How old am I'?\n\n")
    answer = input('Type Y or N:> ')

    if answer == 'Y' or answer == 'yes' or answer =='y' or answer == 'YES' or answer == 'Yes':
        print("\nWell, what are you waiting for? Guess my age:")
        answer = input('\n> ')

        try:
            if int(answer) == info["number"]:
                print("\nOf course. Google, right? \n\n:( ")
            else:
                print("\nWrong! I am {} years old.".format(info["number"]))
                print("\nThat'll be one kidney. I'll take an IOU.")
        except:
            print("\nWrong! I am {} years old.".format(info["number"]))
            print("\nThat'll be one kidney. I'll take an IOU")

    elif answer == 'N' or answer == 'NO' or answer == 'n' or answer == 'no' or answer == 'No':
        print("\nYou must be a old. \n:(")

    else: print("\nOhhh Yeah...")

else: print("Error: {}\n\ntry again later.".format(response.status_code))
