import random

# Generates and returns a random key
def keyGen(alpha):
    key = ""
    for i in range(len(alpha)):
        index = random.randint(0, 25 - i)
        key = key + alpha[index]
        alpha = alpha[:index] + alpha[index + 1:]
    return key


# Encrypts plaintext using a random key and a Caeser cipher
def caesar(plainText):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = keyGen("abcdefghijklmnopqrstuvwxyz")
    print("Random key: ")
    print(alphabet)
    print(key)

    plainText = plainText.lower()

    cipherText = ""
    for ch in plainText:
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
    oddChars = ''
    evenChars = ''
    i = 0
    for ch in plainText:
        if i % 2:
            oddChars = oddChars + ch
        else:
            evenChars = evenChars + ch
        i += 1

    cipherText = oddChars + evenChars
    return cipherText


# Encrypts plaintext using ASCII shift
def ascii_shift(plainText):
    shift = random.randint(1, 25)
    cipherText = ''
    print("Shift: ", shift)
    for ch in plainText:

        cipherText += chr(ord(ch)+shift)

    return cipherText

# Driver
def my_main():
    msg = input("Enter a message to encrypt: ")
    print('Which encryption do you want to use?')
    choice = input('Enter 1 for random Caeser cipher, 2 for transposition, 3 for an ASCII shift: ')
    badInput = True
    if choice.isdigit():
        int_choice = int(choice)
        if int_choice > 0 and int_choice < 4:
            badInput = False;
    while badInput:
        print('Invalid input - try again')
        choice = input('Enter 1 for random Caeser cipher, 2 for transposition, 3 for an ASCII shift: ')
        if choice.isdigit():
            int_choice = int(choice)
            if int_choice > 0 and int_choice < 4:
                badInput = False;
    cipherText = ''
    if choice == '1':
        cipherText = caesar(msg)
    elif choice == '2':
        cipherText = trans(msg)
    else:
        cipherText = ascii_shift(msg)
    print('The encrypted message is: ', cipherText)


if __name__ == '__main__':
    my_main()
