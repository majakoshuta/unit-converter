print("Welcome to the kilometers to miles converter!")
while True:
    try:
        km = int(input("Enter the number of km: "))
        solution = km * 0.6
        print("The solution is " + str(solution) + " miles!")
        answer = str(input("Would you go again? "))
        if answer.lower() == "yes" or answer.lower() == "y":
            None
        elif answer.lower() == "no" or answer.lower() == "n":
            print("Okay, goodbye!")
            break
        else:
            print("Alright, let's convert some more")
    except ValueError:
        print("Please, enter a number!")

