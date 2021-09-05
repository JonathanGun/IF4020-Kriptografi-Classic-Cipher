from math import *

def vigenere_key(string, key):
	key = list(key)
	if len(string) == len(key):
		return key
	else:
		for i in range(len(string) - len(key)):
			key.append(key[i % len(key)])
	return("".join(key))

def vigenere_encrypt(string, key):
	cipher_text = []
	for i in range(len(string)):
		x = (ord(string[i]) + ord(key[i])) % 26
		x += ord('A')
		cipher_text.append(chr(x))
	return("".join(cipher_text))

def vigenere_decrypt(cipher_text, key):
	plain_text = []
	for i in range(len(cipher_text)):
		x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
		x += ord('A')
		plain_text.append(chr(x))
	return("".join(plain_text))

def autovigenere_key(string, autokey):
	autokey = list(autokey)
	if len(string) == len(autokey):
		return autokey
	else:
		for i in range(len(string) - len(autokey)):
			autokey.append(string[i % len(autokey)])
	return("".join(autokey))