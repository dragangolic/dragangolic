print("Hi, welcome to my game!")
print()
print("This game is for all and you have to answer to all questions in such a way that keeps you in the game."
      "Wrong answer and you lose. Good luck!")

print()
print("My name is Dragol. ")
name = input("What is your name?").lower()
age = input("How old are you "+ name + "?")

ready = input("Are you ready? (yes/no)").lower()
if ready == "yes":
    print("Bravo!")
elif ready == "no":
    print("Not a valid option. But, you can continue this time. ")
else:
    print("Not a valid option. But, you can continue this time. ")

character = input("Please, choose one character from the list: python, dog, ice cream, ambulance, cloud:  ")
if character == "python":
    print("  🐍  is a big snake. " + name,", be careful!")
    #print("Sorry, you lose")
elif character == "dog":
    character = input("Ok,do you like to hug or to kiss in public? ")
    if character == "hug":
       print("lol")
       print("  🐶 are the best friends. " + name,", you must be a good friend. You Won!")
    else:
       print("Sorry, you lose")

elif character == "ice cream":
   character = input("Haha, chocolate or vanilla? ")
   if character == "chocolate":
       print("  🍦,have some calories, "+ name, "be careful")
   else:
       print("Sorry you lose!")
elif character == "ambulance":
   character = input("What would you be rather driver or doctor? ")
   if character == "doctor":
       print("  🚑, help other people. "+ name,"That is nice! You Won!!")
   else:
       print("Sorry, you lose!")
elif character == "cloud":
   character = input("If you fall you can hurt yourself. Choose between mattress and leaves ")
if character == "mattress":
  print("  ☁  " + name, " u must be a dreamer! That is cool! You Won!!!")
else:
   # print("Sorry you lose!!")
   print("It was pleasure to play together")
print("The Game is Over")
