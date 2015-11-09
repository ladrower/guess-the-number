from random import randint

i = 0
MIN = 0
MAX = 99
number = randint(MIN, MAX)
guessed = False

print "We have generated the integer number between " + str(MIN) + " and " + str(MAX) + ". Please try to guess it.\r\n"

while not guessed:
    i += 1
    try:
        guess = int(raw_input('Enter your guess: '))
        guessed = number == guess
        if not guessed:
            print "Your guess is " + ("smaller" if number > guess else "greater") + " than our number"

    except ValueError:
        print "Incorrect input"

    if not guessed:
        print "Please try again\r\n"

print "You are right. The number was " + str(number) + ". Iterations taken: " + str(i)
