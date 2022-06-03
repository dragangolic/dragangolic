import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def about_me(name, profession, pet, hobby):
    print(Fore.RED + "Hi, I am", name)
    print(Back.GREEN + "I am a", profession)
    print(Fore.MAGENTA + "And I have ", pet)
    print(f"{Back.CYAN} I love to play", hobby)
about_me("Dragan", "programmer", "bees", "guitar")
print(f"{Fore.BLUE } I hope you are going to like my small repo project")
print(f"{Style.NORMAL}{Fore.LIGHTBLUE_EX}{Back.YELLOW} Enjoy with us on this beautiful trip")
print()
def vacation(country, place, date, partner, type):
    print("We where planing trip to ", country)
    print("The capital is", place)
    print("We planed a trip at", date)
    print("I love to travel with my", partner)
    print("It is always fun when we have", type)
vacation ("Florida","Tallahassee","2022.02.14", "spouse", "active vacation")
print()
def driving(car, duration, distance, est_fuel_costs):
    print("We will drive", car)
    print("Total trip is ", duration)
    print("Total mileage is ", distance)
    print("Will spend roughly ", est_fuel_costs)
driving ("Dodge Ram1500 Big Horn", "19hr6min.", "1,143mi", "$435.29")

places_to_visit = ("Washington DC", "Cape Charles", "Key West","Miami")
places_for_bees = ("Blue Mountain - Georgia", "Nashville-Tennessee")
# print(places_to_visit)
# print(places_for_bees)
stops = int(input("Enter the number of stops:"))
if stops < 2:
    print(places_for_bees)
elif stops > 5:
    print(places_to_visit + places_for_bees)
else:
    print("Sorry,not enough time for visiting nice cities. Bees need nectar!")


gallon = int(input("How many gallons we need?: "))
def miles_per_gallon():
    return gallon * 4.50
print("$", miles_per_gallon)


