import random

stages = ["""
        ------------
        |          | 
        |          o
        |         \\|/
        |          |
        |         / \\
       ___
             """,
             """
        ------------
        |          |
        |          o
        |         \\|/
        |          |
        |         /
       ___
                
             """,
             """
        ------------
        |          |
        |          o
        |         \\|/
        |          |
        |
       ___
             """,
             """
        ------------
        |          |
        |          o
        |         \\|
        |          |
        |
       ___
             """,
             """
        ------------
        |          |
        |          o
        |          |
        |          |
        |
       ___
             """,
             """
        ------------
        |          |
        |          0
        |
        |
        |
       ___
             """,
             """
        ------------
        |          |
        |
        |
        |
        |
       ___ 
             """
    ]


        
#These are the random words 
words = []

letterGuessed = []

game_going = True

random_word = random.choice(words)

message = "The word found was "+random_word

array = list(random_word)

hidden = list('-'*len(array))
    
lost = False
won=False
times = 0
exit = False
print("\nThe word contais",len(random_word),"letters")
while game_going:
    print(stages[len(stages) - times - 1])
    print("\n")
    print("".join(hidden))
    letter = input("\nGuessed a letter: ").lower()[0]
    if letter == "exit":
        exit = True
        loop=False
    if letter in letterGuessed:
        print("\nThis letter was already Used.")
    elif letter in random_word:
        print("\nCorrect letter!!!!")
    else:
        print("\nThe letter is wrong :(")
        times += 1 
    letterGuessed.append(letter)
    if exit == False:
        print("Letters used:",", ".join(set(letterGuessed)))
    for i, lt in enumerate(array):
        if letter == lt:
            hidden[i] = lt
    if times == 6:
        lost = True
        break
    if '-' not in hidden:
        won = True
        game_going = False
    


if lost:
    print("\nThe word not found was",random_word)
    print("You lost!")
    print("\n")
    print(stages[0])
    print("\nYOUR ARE DEAD\n")
if won:
    print("\n"+message)
    print("Congratulations!!, you have found the hidden random word!!!!!")

if exit:
    print("You left Game")
    
