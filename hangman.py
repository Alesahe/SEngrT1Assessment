from random import randint

list = [] 

#add words to list
with open("wordlist.txt","r") as f:
    for line in f:
        line = line.strip().lower()
        list.append(line)

word = list[randint(0, len(list))]
print(word)
display = ""
for i in word:
    display+="_"

def print_hangman():
    with open("longKatASCII.txt", "r") as f:
        for line in f:
            print(line)
    print("\n")
    print(display)

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

print("Welcome to HangKat!")
print("Meet LongKat, a ")
print("Instructions: ")
print(" - You may guess letters or the full word, nothing in between")
print(" - You have [] tries to correctly guess the word!")
print_hangman()
while word!=display:
    guess = input("What is your guess? ")
    display = check_letters(guess, word, display)
    print_hangman()
print("You won!")