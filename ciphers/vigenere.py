from ciphers.base import Cipher


class VigenereCipher(Cipher):
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
    
    def encrypt(msg: str) -> str:
        # TODO
        return msg + "ASD"

    def decrypt(msg: str) -> str:
        # TODO
        return "ASD" + msg


class AutoVigenereCipher(VigenereCipher):
    def encrypt(msg: str) -> str:
        # TODO
        return msg + "ASDdsa"

    def decrypt(msg: str) -> str:
        # TODO
        return "dsaASD" + msg


class FullVigenereCipher(VigenereCipher):
    def encrypt(msg: str) -> str:
        # TODO
        return msg + "ASDasd"

    def decrypt(msg: str) -> str:
        # TODO
        return "asdASD" + msg


class ExtendedVigenereCipher(VigenereCipher):
    def encrypt(msg: str) -> str:
        # TODO
        return msg + "ASDdsa1"

    def decrypt(msg: str) -> str:
        # TODO
        return "1dsaASD" + msg
