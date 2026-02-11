secret_number = 7

guess_count = 0

while guess_count < 3:
    guess = int(input("Guess the number: "))
    if guess == secret_number:
        print("Congratulations! You guessed the number.")
        break
    else:
        print("Wrong guess. Try again.")
    guess_count += 1