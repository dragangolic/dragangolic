import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def about_me(name, profession, pet, hobby):
    print(Fore.RED + "Hi, I am", name)
    print(Back.GREEN + "I am a", profession)
    print(Fore.MAGENTA + "And I have ", pet)
    print(f"{Back.CYAN} I love to play", hobby)
about_me("Dragan", "programmer", "bees", "guitar")
print(f"{Fore.BLUE } I hope you are going to like my small repo projects")
print(f"{Style.NORMAL}{Fore.LIGHTBLUE_EX}{Back.YELLOW} Have a lovely day")
