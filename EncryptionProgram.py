import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"chars : {chars}")  characters used
# print(f"key : {key}") key used

# MessageEncryption
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original message: {plain_text}")
print(f"encrypted message: {cipher_text}")

# MessageDecryption
cipher_text = input("Enter a message to encrypt: ")
plain_text = ""

for letter in cipher_text:
    index = chars.index(letter)
    plain_text += chars[index]

print(f"encrypted message: {cipher_text}")
print(f"original message: {plain_text}")
