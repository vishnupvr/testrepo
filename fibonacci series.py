import random
secretNumber = random.randint(1, 20)
print("Number between 1 and 20.")

for guessesTaken in range(1, 6):
	print('Take a guess')
	guess = int(input())
	
	if guess < secretNumber:
		print('Your guess is too low')
	elif guess > secretNumber:
		print('Yout guess is too high')
	else:		
		print("Good job! You guessed my number in " + str(guessesTaken) + " guesses")
		break

print("The number I was thinking of was " + str(secretNumber))
