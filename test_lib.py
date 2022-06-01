
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