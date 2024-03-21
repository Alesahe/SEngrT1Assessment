from random import randint

list = [] #list of words
stage = 0 #the stage of longKat's slow and painful death the program is up to currently
prevGuesses = [] #stores the previous words and letters the player has guessed

#add words to list
with open("wordlist.txt","r") as f:
    for line in f:
        line = line.strip().lower()
        list.append(line)

#selects a random word from the list and initialises the string "display" with the correct number of underscores
word = list[randint(0, len(list))]
display = ""
for i in word:
    display+="_"

#prints out the corresponding ASCII hangman image
def print_hangman():
    with open("longKatASCII_"+str(stage)+".txt", "r") as f:
        for line in f:
            print(line)
    print("\n")
    print(display)
    print("\n")

#adds newly-guessed correct answers
def check_letters(guess, word, display):
    guess = guess.lower()
    if guess==word:
        display = word
    else:
        temp = display
        display=""
        for i in range(len(word)):
            if guess==word[i]:
                display+=guess
            else:
                display+=temp[i]
    return display

#introduction flavourtext
with open("welcomeFlavourtext.txt", "r") as f:
    for line in f:
        print(line)
    print("\n")

#instructions
with open("instructions.txt", "r") as f:
    for line in f:
        print(line)
    print("\n")

#print word
print_hangman()

#iterates until the game is over
while word!=display and stage!=9:
    guess = input("What is your guess? ")
    print("\n")
    if guess in prevGuesses:
        print("You've already guessed that!\n")
    else:
        temp = display
        display = check_letters(guess, word, display)
        if temp==display:
            stage+=1
        if stage!=9:
            print_hangman()
    prevGuesses.append(guess)

#endgame messages woo
if stage!=9:
    print("You won! LongKat is freed from her fetters and the two of you can go back to sharing BFF necklaces and developing your newfound knack for password-cracking!")
else:
    print("LongKat is shaking her head. All the alarms have been set off - now Diana knows that you've been there.")
    print("womp womp")
    print("sadgers")