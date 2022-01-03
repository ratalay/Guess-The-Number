import random

print("Hello, what's your name?")
name = input()

print("Well, " + name + ", let's guess the number I have in mind, it's between 1 & 20!")
secretNumber = random.randint(1, 20)

print("Take a guess")
for guessesTaken in range (1, 7):
    guess = int(input())
    if guess < secretNumber:
        print("That's low!")
    elif guess > secretNumber:
        print("That's high!")
    else:
        break

if guess == secretNumber:
    print("Well done! It took you " + str(guessesTaken) + " guesses to find my number")
else:
    print("The number I took was " + str(secretNumber) + ". Better luck next time!")
