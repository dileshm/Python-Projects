import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

print("---------------------------------------------------------------")
print("-------------------MESSAGE ENCRYPTION SERVICE------------------")
print("---------------------------------------------------------------")

# Message Encryption
plain_text = input("ENTER A MESSAGE TO ENCRYPT: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"ORIGINAL MESSAGE: {plain_text}")
print(f"ENCRYPTED MESSAGE: {cipher_text}")

# Message Decryption
while True:
    decrypt_choice = input(
        "DO YOU WANT TO DECRYPT THE MESSAGE (YES/NO): ").lower()

    if decrypt_choice == 'yes':
        plain_text = ""
        for letter in cipher_text:
            index = key.index(letter)
            plain_text += chars[index]

        print(f"ENCRYPTED MESSAGE: {cipher_text}")
        print(f"ORIGINAL MESSAGE: {plain_text}")
        print("YOUR MESSAGE HAS BEEN DECRYPTED.")
        break
    else:
        print("ENCRYPTION/DECRYPTION PROCESS ENDED.")
        break
