import os

SECRETWORD = 'perfume'
encryptedWord = len(SECRETWORD) * '*'
attempts = 0
while encryptedWord!=SECRETWORD:
 
    print(f'\nSecret word is: {encryptedWord}')
    inputLetter = input('\nType a letter for the secret word.\n')
    modSecretWord = SECRETWORD

    if len(inputLetter) > 1:
        print('\nType a single letter for each input!')
    elif inputLetter in modSecretWord:
        attempts +=1
        for letter in modSecretWord:
            if letter == inputLetter:
                letterIndex = modSecretWord.find(letter)
                replacementLetter = modSecretWord[letterIndex]
                modSecretWord = modSecretWord[0:letterIndex]+ '*' + modSecretWord[letterIndex+1:]
                encryptedWord = encryptedWord[0:letterIndex]+ replacementLetter + encryptedWord[letterIndex+1:] 

os.system('clear')
print(f'You won! The secret word is: {encryptedWord}')
print(f'Total amount of attempts: {attempts}!')
