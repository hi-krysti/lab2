print("Hello and welcome to the Number Analyzer!")
name = input("What is your name? \n> ")

print("Welcome, " + name + ". Please enter an integer between 1 and 100:")
num = int(input("> "))


if (num % 2 != 0) and 0 < num < 60:
    print("Thank you, " + name + ". Your integer is odd and less than 60.")
elif (num % 2 == 0) and 2 <= num < 25:
    print("Thank you, " + name + ". Your integer is even and less than 25.")
elif (num % 2 == 0) and 26 <= num < 61:
    print("Thank you, " + name + ". Your integer is even and between 26 and 60 inclusive.")
elif (num % 2 == 0) and 60 < num < 101:
    print("Thank you, " + name + ". Your integer is even and greater than 60.")
elif (num % 2 != 0) and 60 < num < 100:
    print("Thank you, " + name + ". Your integer is odd and greater than 60.")
else:
     print("I'm sorry, " + name + " that entry is invalid.")

cont = input("Would you like to enter another integer? y/n \n> ")

while cont == "y":
    print("Please enter an integer between 1 and 100:")
    num = int(input("> "))
    if (num % 2 != 0) and 0 < num < 60:
        print("Thank you, " + name + ". Your integer is odd and less than 60.")
    elif (num % 2 == 0) and 2 <= num < 25:
        print("Thank you, " + name + ". Your integer is even and less than 25.")
    elif (num % 2 == 0) and 26 <= num < 61:
        print("Thank you, " + name + ". Your integer is even and between 26 and 60 inclusive.")
    elif (num % 2 == 0) and 60 < num < 101:
        print("Thank you, " + name + ". Your integer is even and greater than 60.")
    elif (num % 2 != 0) and 60 < num < 100:
        print("Thank you, " + name + ". Your integer is odd and greater than 60.")
    else:
        print("I'm sorry, " + name + " that entry is invalid.")
    cont = input("Would you like to enter another integer? y/n \n> ")
else:
    print("Thank you, " + name + ". Have a great day!")