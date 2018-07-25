import random
number = random.randint(1, 100)
name = raw_input("Enter your name:")
print (name)
while True:
    print('Dear,' + name + ',Guess a number between 1 and 100')
    guess = input()
    i = int(guess)
    if i == number:
        print('Bravo......' + name + 'You won!!!')
        break
    elif i < number:
               print('ohhhhh,' + name + ',Your guess is too high.......Try Higher')
    elif i > number:
               print('wow,' + name + ' Your guess is too low.......Try Lower')
