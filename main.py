import random


with open("namelist.txt", "r") as f:
    names = f.readlines()

name = random.choice(names)[:-1]

allowed_wrong_guesses = 5
guesses = []
done = False

print("Você consegue adivinhar o pokémon? Vamos começar!")

while(done == False):
    for letter in name:
        if letter.lower() in guesses:
            print(letter, end=" ")

        else:
            print("_", end=" ")

    print("")

    print(f"Diga uma letra! Você tem {allowed_wrong_guesses} tentaivas sobrando.")
    guess = input("")
    guesses.append(guess.lower())

    if(guess.lower() not in name.lower()):
        print("O nome não tem essa letra!")

        allowed_wrong_guesses -= 1 
        if(allowed_wrong_guesses <= 0):
            print("Oh não, acabaram as tentativas!")
            break

    done = True
    for letter in name:
        if letter.lower() not in guesses:
            done = False


if(done):
    print(f"Você acertou! era um {name}.")
else:
    print(f"Você quase conseguiu! o pokémon era {name}.")   
