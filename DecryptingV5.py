#Caeser Cipher WORKING BABY
alphabet =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

dragonalphabet = ['d','r','a','g','o','n','b','c','e','f','h','i','j','k','l','m','p','q','s','t','u','v','x','y','z']
import random

def mainsub():
    word_sub = input("Enter the word you want to substitute with ")
    plain_message = input("Enter your message in plaintext ")
    plain_message = plain_message.lower()
    sub_list = sub_shift(word_sub)
    print (sub_list)
    sub_cypher_encrypt(plain_message,sub_list)
    menu()

def sub_shift(word):
    sub_cypher = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    count = 0
    for i in range(0,len(word)):
        if word[i] in sub_cypher:
            sub_cypher.remove(word[i])
    for i in range(0,len(word)):
        if word[i] in sub_cypher:
            count =+1
        else:
            sub_cypher.insert((i-count),word[i])
    return sub_cypher


def sub_cypher_encrypt(message,p_sub_list):
    encoded = ""
    for i in range(0,len(message)):
        if message[i] in p_sub_list:
            encodedletter = alphabet.index(message[i])
            encodedletter = encodedletter % 26
            encoded += p_sub_list[encodedletter]
        else:
            encoded +=  message[i]
    encoded = encoded.upper()
    print (encoded)

def mainencrypt():
    plain_message = input("Enter your message in plaintext ")
    key = int(input("Enter your key "))
    plain_message = plain_message.lower()
    encrypt(plain_message,key)
    menu()

def encrypt(message,encodekey):
    encoded = ""
    for i in range(0,len(message)):
        if message[i] in alphabet:
            encodedletter = alphabet.index(message[i])+encodekey

            encodedletter = encodedletter % 26
            encoded += alphabet[encodedletter]
        else:
            encoded +=  message[i]
    encoded = encoded.upper()
    print (encoded)

def mainencryptDragon():
    plain_message = input("Enter your message in plaintext ")
   # key = int(input("Enter your key "))
    key = 0
    plain_message = plain_message.lower()
    dragonencrypt(plain_message,key)
    menu()

def dragonencrypt(message,encryptkey ):
    dragonencrypt = ""
    for i in range(0,len(message)):
        if message[i] in alphabet:
            encryptletter = alphabet.index(message[i])#+encryptkey

            encryptletter = encryptletter % 26
            dragonencrypt += dragonalphabet[encryptletter]
        else:
            dragonencrypt +=  message[i]
    dragonencrypt = dragonencrypt.upper()
    print (dragonencrypt)

def maindecrypt():
    decode_message = input("Enter your message in encoded text ")
    key = int(input("Enter the key to decode it(assuming you go left) "))
    decode_message = decode_message.lower()
    decrypt(decode_message,key)
    menu()

def decrypt(message,decodekey):
    decoded = ""
    for i in range(0,len(message)):
        if message[i] in alphabet:
            decodedletter = alphabet.index(message[i])-decodekey
            decodedletter = decodedletter % 26
            decoded += alphabet[decodedletter]
        else:
            decoded += message[i]
    decoded = decoded.upper()
    print (decodekey,'.',decoded)

def unknown():
    decode_message = input("Enter your message in encoded text ")
   # key = int(input("Enter the key to decode it(assuming you go left) "))
    decode_message = decode_message.lower()
    decryptunknown(decode_message)
    menu()

def decryptunknown(message):
    for key in range (0,26):
        decrypt(message,key)


def encryptgame():
    health = 3
    game_message = input("Enter your message in encoded text ")
    key = random.randrange(1,25)
    encrypt(game_message,key)
    print("Guess what key value was used to encrypt the message. You have three lives")
    answer = int(input(""))
    guess(health,answer,key)

def guess(lives,guess_answer,realkey):
    if guess_answer != realkey:
        lives = lives - 1
        print("You have entered the incorrect answer. Your current lives are",lives)
        if lives == 0:
            print("You have lost the game. Press any button to return to menu")
            input()
            menu()
        else:
            print("try to guess again")
            guess_answer = int(input(""))
            guess(lives,guess_answer,realkey)
    print("Congratulations you have won with ",lives," left! Press any key to go back to the menu")
    input()
    menu()
def shift_decrypt():
    print ("Shift decrypt")

def menu():
    print()
    print("Hello welcome to the encryption menu! ")
    print("Choose your option: ")
    print("1. You want to encrypt a message ")
    print("2. You want to decrypt a message with a known key ")
    print("3. If you want to play a decrypting game ")
    print("4. FOR DRAGON ENCRYPTING")
    print("5. for decrypting with an unknown key")
    print("6. For shift decrypting")
    print("7. For shift Cypher")
    print("0. If you want to quit ")
    answer = int(input(""))
    if answer == 1:
        mainencrypt()
    elif answer == 2:
        maindecrypt()
    elif answer == 3:
        encryptgame()
    elif answer == 0:
        exit()
    elif answer ==4:
        mainencryptDragon()
    elif answer ==5:
        unknown()
    elif answer ==6:
        shift_decrypt()
    elif answer ==7:
        mainsub()
    else:
        print("Please choose a correct option")
        menu()

menu()
