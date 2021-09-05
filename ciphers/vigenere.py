from ciphers.base import Cipher


class VigenereCipher(Cipher):
    def generate_key(string, key):
        key = list(key)
        if len(string) == len(key):
            return key
        else:
            for i in range(len(string) - len(key)):
                key.append(key[i % len(key)])
        return("".join(key))

    def _encrypt(msg: str, key: str) -> str:
        cipher_text = []
        for i in range(len(msg)):
            x = (ord(msg[i]) + ord(key[i])) % 26
            x += ord('A')
            cipher_text.append(chr(x))
        return("".join(cipher_text))

    def encrypt(msg: str, key: str) -> str:
        key = VigenereCipher.generate_key(msg, key)
        return VigenereCipher._encrypt(msg, key)

    def _decrypt(msg: str, key: str) -> str:
        plain_text = []
        for i in range(len(msg)):
            x = (ord(msg[i]) - ord(key[i]) + 26) % 26
            x += ord('A')
            plain_text.append(chr(x))
        return("".join(plain_text))

    def decrypt(msg: str, key: str) -> str:
        key = VigenereCipher.generate_key(msg, key)
        return VigenereCipher._decrypt(msg, key)


class AutoVigenereCipher(VigenereCipher):
    def generate_key(string, key):
        autokey = list(key)
        if len(string) == len(autokey):
            return autokey
        else:
            for i in range(len(string) - len(autokey)):
                print(i)
                autokey.append(string[i % len(autokey)])
        return("".join(autokey))

    def encrypt(msg: str, key: str) -> str:
        key = AutoVigenereCipher.generate_key(msg, key)
        return VigenereCipher._encrypt(msg, key)

    def decrypt(msg: str, key: str) -> str:
        ret = ""
        for i in range(len(msg)):
            x = (ord(msg[i]) - ord(key[i]) + 26) % 26
            x += ord('A')
            key += chr(x)
            ret += chr(x)
        return ret


class FullVigenereCipher(VigenereCipher):
    def generate_key(string, key):
        # TODO
        return VigenereCipher.generate_key(msg, key)

    def encrypt(msg: str, key: str) -> str:
        key = FullVigenereCipher.generate_key(msg, key)
        return VigenereCipher._encrypt(msg, key)

    def decrypt(msg: str, key: str) -> str:
        key = FullVigenereCipher.generate_key(msg, key)
        return VigenereCipher._decrypt(msg, key)


class ExtendedVigenereCipher(VigenereCipher):
    allow_byte = True

    def generate_key(string, key):
        # TODO
        return VigenereCipher.generate_key(msg, key)

    def encrypt(msg: str, key: str) -> str:
        key = ExtendedVigenereCipher.generate_key(msg, key)
        return VigenereCipher._encrypt(msg, key)

    def decrypt(msg: str, key: str) -> str:
        key = ExtendedVigenereCipher.generate_key(msg, key)
        return VigenereCipher._decrypt(msg, key)
