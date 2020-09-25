# lotterypicker
# to random pick numbers for various online lottery games
# advanced number generator
#lottery
import random
print()
print('Welcome to my lottery number generator')
print('**** by Kenneth Mundell 2020 *********')

balls_total = int(input('What is the range of the main balls 1 - '))
balls_count = int(input('How many main balls are there? '))
print()
star_total = int(input('What is the range of the bonus balls 1 - '))
star_count = int(input('How many bonus balls are there? '))
print()

print('Main numbers are: ')
for i in range(balls_count):
    print(random.randint(1, balls_total))
print()

print('Bonus balls are')
for x in range(star_count):
    print(random.randint(1, star_total))
print('Good luck!')
