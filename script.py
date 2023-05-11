import random
from hangman_art import stages, logo
from hangman_words import word_list

listOfWords = word_list
randomWord = random.choice(listOfWords)
isGameWon = False
wordBlanks = ['_'] * len(randomWord)
mistakes = 0

print(logo)

while not isGameWon:
    print('\n', ' '.join(wordBlanks))
    usersChoice = input('Enter your letter: ')
    
    for i, letter in enumerate(randomWord):
        if usersChoice == letter:
            wordBlanks[i] = usersChoice

    if not randomWord.__contains__(usersChoice):
        mistakes += 1
        print(stages[- mistakes])
        
    if (''.join(wordBlanks)) == randomWord or mistakes == 7:
        print('\n', ' '.join(wordBlanks))
        isGameWon = True
    
print('Game Over')

    