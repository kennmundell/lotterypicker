# Lottery list
import random
import os
print()
os.system('cls')
print("Welcome to my euromillions lottery number picker...")
print()

l = list(range(0))
s = list(range(0))


def picker():
    for i in range(5):
        number_a = random.randint(1,50)

        l.append(number_a)
    if(len(set(l)) == len(l)):
        print("All numbers are unique")
        
    else:
        l.remove(number_a)
        number_b = random.randint(1,50)
        l.append(number_b)

    print(l)
    for i in range(2):
        number_d = random.randint(1,12)

        s.append(number_d)
    if(len(set(s)) == len(s)):
        print("All numbers are unique")
        
    else:
        s.remove(number_d)
        number_d = random.randint(1,12)
        s.append(number_d)
    print(s)

picker()
if(len(set(l)) != len(l)):
    os.system('cls')
    l.clear()
    s.clear()
    picker()

