import random


# Generates and returns a random key
def keyGen(alpha):
    key = ""
    for i in range(len(alpha)):
        index = random.randint(0, 25 - i)
        key = key + alpha[index]
        alpha = alpha[:index] + alpha[index + 1:]
    return key


# Encrypts plaintext using a random key and a Caesar cipher
def caesar(plainText):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = keyGen(alphabet)
    print("Random key: ")
    print(alphabet)
    print(key)

    cipherText = ""
    for ch in plainText.lower():
        idx = alphabet.find(ch)
        if idx >= 0:
            cipherText += key[idx]
        elif ch.isdigit():
            cipherText += ch
        else:
            cipherText += ' '

    return cipherText


# Encrypts plaintext using transposition cipher
def trans(plainText):
    return plainText[1::2] + plainText[0::2]


# Encrypts plaintext using ASCII shift
def ascii_shift(plainText):
    shift = random.randint(1, 25)
    cipherText = ''
    print("Shift: ", shift)
    for ch in plainText:
        cipherText += chr(ord(ch) + shift)

    return cipherText


# Driver
def my_main():
    msg = input("Enter a message to encrypt: ")
    print('Which encryption do you want to use?')

    while True:
        choice = input('Enter 1 for random Caeser cipher, 2 for transposition, 3 for an ASCII shift: ')
        if choice.isdigit():
            int_choice = int(choice)
            if int_choice > 0 and int_choice < 4:
                break
        print('Invalid input - try again')

    if choice == '1':
        cipherText = caesar(msg)
    elif choice == '2':
        cipherText = trans(msg)
    else:
        cipherText = ascii_shift(msg)
    print('The encrypted message is: ', cipherText)

    while True:
        userContinue = input("Repeat? Enter y to repeat or q to quit: ")
        if userContinue == 'y':
            my_main()
            break
        elif userContinue == 'q':
            break


if __name__ == '__main__':
    my_main()
