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
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")

# Message Decryption Loop
while True:
    decrypt_choice = input(
        "Do you want to decrypt the message? (yes/no): ").lower()

    if decrypt_choice == 'yes':
        plain_text = ""
        for letter in cipher_text:
            index = key.index(letter)  # Correctly use 'key' for decryption
            plain_text += chars[index]

        print(f"Encrypted message: {cipher_text}")
        print(f"Original message: {plain_text}")
        print("Your message has been decrypted.")
        break
    else:
        print("Encryption/Decryption process ended.")
        break
