import random
import hello

while True:
    my_rand = random.randrange(1,21)
    while True:
        my_guess = int(input("Guess: "))
        if my_guess == my_rand:
            print("Good job")
            break
        elif my_guess > my_rand:
            print("guess lower")
        else:
            print("guess higher")
            
    my_cont = input("Continue? ")
    if my_cont != "Yes":
        break

print("Thanks for playing")
a,b,c = hello.my_func(4)
print(a)
print(b)
print(c)

