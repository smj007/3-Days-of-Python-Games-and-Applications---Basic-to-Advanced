#Begin your code
import random
name = input("Enter your name: ")

print("Hello ", name)

print("-----------")

def hangman():
    word = random.choice(["sai", "avengers", "yolo", "deeplearning", "applesauce", "faasos", "anaconda", "webstorm", "shaji", "bsdk"])
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessMade = ''

    while len(word) > 0:
        main = ""
        missed = 0

        for letter in word:
            if letter in guessMade:
                main = main + letter
            else:
                main = main + "_" + " "

        if main == word:
            print(main)
            print("You win the game")
            break

        print("Guess the word: ", main)
        guess = input()

        if guess in validLetters:
            guessMade = guessMade + guess
        else:
            print("Enter a valid character")
            guess = input()

        if guess not in word:
            turns = turns - 1

        if turns == 9:
            print("9 turns left")
            print("------------")

        if turns == 8:
            print("8 turns left")
            print("------------")
            print("      O      ")

        if turns == 7:
            print("7 turns left")
            print("------------")
            print("      O     ")
            print("      |     ")

        if turns == 6:
            print("6 turns left")
            print("------------")
            print("      O     ")
            print("      |     ")
            print("     /      ")

        if turns == 5:
            print("5 turns left")
            print("------------")
            print("      O     ")
            print("      |     ")
            print("     / \    ")

        if turns == 4:
            print("4 turns left")
            print("------------")
            print("      O     ")
            print("     /|     ")
            print("     / \    ")


        if turns == 3:
            print("3 turns left")
            print("------------")
            print("      O     ")
            print("     /|\     ")
            print("     / \    ")

        if turns == 2:
            print("2 turns left")
            print("------------")
            print("      O |   ")
            print("     /|\    ")
            print("     / \    ")

        if turns == 1:
            print("1 turn left")
            print("You are nearing the end my son")
            print("------------")
            print("      O_|   ")
            print("     /|\    ")
            print("     / \    ")

        if turns == 0:
            print("NO turns left")
            print("Your player is now dead")
            print("------------")
            print("      |   ")
            print("     /|\    ")
            print("     / \    ")
            break


print("Try to guess the correct word in under 10 attempts")
hangman()
print()
