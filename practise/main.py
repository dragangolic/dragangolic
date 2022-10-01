
# Inheritance
# inherits (all attributes and func)
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is working..")


class SoftwareEngineer(Employee):#  this is also an overriding
    def __init__(self, name, age, salary,level):#  because we have the same function in base function we will not go
        super().__init__(name, age, salary)#  with the same code we will call the initializor from parent class
        self.level = level

    def work(self):#  overriding of the function in child class
        print(f"{self.name} is coding..")

    def debug(self):
        print(F"{self.name} is debugging..")


class Designer(Employee):
    def work(self):
        print(f"{self.name} is designing.")

    def draw(self):
        print(F"{self.name} is drawing..")


se = SoftwareEngineer("Kirk", 30, 6000, "Junior")
print(se.name, se.age)
se.work()
print(se.level)
print(se.debug())

d = Designer("Phil", 70, 7000)
print(d.name, d.age)
d.draw()
d.work()

#  Polymorphism


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        # TODO: ADD PROPERTIES
        self.author = author
        self.pages = pages
        self.price = price
        #  self.__secret = "This is a secrete attribute" if we try to access
        #  print(b2.__secret) it's not going to work

    #  TODO: CREATE INSTANCE METHODS
    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def setdiscount(self, amount):
        self._discount = amount  # underscore in the name is telling other\
        # developers do not use it in your code

# TODO: CREATE SOME BOOK INSTANCES


b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

# TODO: PRINT THE PRICE OF THE BOOK1
print(b1.getprice())

# TODO: TRY SETTING THE DISCOUNT
print(b2.getprice())
b2.setdiscount(0.25)
print(b2.getprice())

# TODO: PROPERTIES WITH DOUBLE UNDERSCORES ARE HIDDEN BY THE INTERPRETER


# Checking class types and instances

class Book:
    def __init__(self, title):
        self.title = title

class Newspaper:
    def __init__(self, name):
        self.name = name

# create some instances of the class


b1 = Book("The Catcher in the Rye")
b2 = Book("The grapes of wrath")
n1 = Newspaper("The Washington Post")
n2 = Newspaper("The New York Times")

# TODO: USE TYPE() TO INSPECT OBJECT TYPE
print(type(b1))
print(type(n1))

# TODO: COMPARE TWO TYPES TOGETHER
print(type(b1) == type(b2))  # True
print(type(b1) == type(n2))  # False

# TODO: USE ISINSTANCE TO COMPARE A SPECIFIC INSTANCE TO KNOWN TYPE
print(isinstance(b1, Book))  # True
print(isinstance(n1, Newspaper))  # True
print(isinstance(n2, Book))  # False
print(isinstance(n2, object))  # True

#  CLASS METHODS AND MEMBERS


class Book:
    #  TODO: PROPERTIES DEFINED AT THE CLASS LEVEL ARE SHARED BY ALL INSTANCES
    BOOK_TYPES = ("HARDCOVER", "PAPER")

    #  TODO: DOUBLE- UNDERSCORE PROPERTIES ARE HIDDEN FROM OTHER CLASSES
    __booklist = None

    #  TODO: CREATE A CLASS METHOD
    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES

    #  TODO: CREATE A STATIC METHOD
    @staticmethod
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

    # Instance methods receive a specific object instance as an argument
    #  and operate on data specific to that object instance
    def setTitle(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not valid book type")
        else:
            self.booktype = booktype

# TODO: ACCESS THE CLASS ATTRIBUTE
print("Book types: ", Book.getbooktypes())

# TODO: CREATE SOME BOOK INSTANCES
b1 = Book("Title 1", "HARDCOVER")
b2 = Book("Title 2", "PAPERBACK")

# TODO: USE THE STATIC METHOD TO ACCESS A SINGLETON OBJECT
thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)
