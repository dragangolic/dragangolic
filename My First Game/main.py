print("Hi, welcome to my game!")
print("My name is Dragol. ")
name = input("What is your name?").upper()
age = input("How old are you "+ name + "?")

# if age < 5:
#     print("Thank you", name, "but this game is for older gamers")
# if age > 5:
#     print("Great", name, "let's get started with easy questions 😀")

ready = input("Are you ready? (yes/no)").lower()
if ready == "yes":
    print("Bravo!")
elif ready == "no":
    print("Ok, c u next time " + name, "! Good luck, the Game is Over!")
else:
    print("Not a valid option. You lose. ")


