import os

secret_word = 'perfume'
right_letters = ''
attempts = 0

while True:
    inputLetter = input('\nType a letter for the secret word.\n')

    if len(inputLetter) > 1:
        print('\nType a single letter for each input!')
        continue

    if inputLetter in secret_word:
        attempts +=1
        right_letters += inputLetter
    
    final_word = ''
    for secret_letter in secret_word:
        if secret_letter in right_letters:
            final_word += secret_letter
        else:
            final_word += '*'
    print(final_word)   
    
    if final_word == secret_word:
        os.system('clear')
        print(f'You won! The secret word is: {final_word}')
        print(f'Total amount of attempts: {attempts}!')
        break
