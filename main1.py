
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
