from vigenere_def import *
import re

string = input("Enter plaintext message: ").upper()
string = re.sub(r'[0-9]+', '', string)
string = re.sub(r'[^\w]', ' ', string)
string = re.sub(r"\s+", "", string)
print("Your message is:", string)

keyword = input("Enter key: ").upper()
keyword = re.sub(r'[0-9]+', '', keyword)
keyword = re.sub(r'[^\w]', ' ', keyword)
keyword = re.sub(r"\s+", "", keyword)
print("Your key is:", keyword)
print()

key = vigenere_key(string, keyword)
autokey = autovigenere_key(string, keyword)
print("Generated key:", key)
print("Generated autokey:", autokey)
print()

encrypted = vigenere_encrypt(string, key)
autoencrypted = vigenere_encrypt(string, autokey)

print("Encrypted message:", encrypted)
print("Encrypted message (with autokey):", autoencrypted)
print()
print("Decrypted message:", vigenere_decrypt(encrypted, key))
print("Decrypted message (with autokey):", vigenere_decrypt(autoencrypted, autokey))