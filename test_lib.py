
secret_num = 7
guess_count = 0
guess_limit = 2
while guess_count<guess_limit:
    guess = int(input("What is the secret number? (1-10)"))
    guess_count += 1
    if guess == secret_num:
        print("GREAT")
        break
else:
    print("Sorry,more luck next time.")
# just the comment

class School():
    def __init__(self):
        self.__goingtoschool()
    def learning(self):
        print("OOP and encapsulation")
    def study(self):
        print("Python")
    def __goingtoschool(self):
        print("I love coding")
laptop = School()
laptop.learning()
laptop1 = School()
laptop1.study()
class addingSchool(School):
    def __init__(self):
        School.__init__(self)
        self.__sum = 0

