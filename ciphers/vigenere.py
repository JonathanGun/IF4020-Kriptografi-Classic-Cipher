from ciphers.base import Cipher


class VigenereCipher(Cipher):
    def preprocess_key(self):
        n = len(self.msg) - len(self.key)
        for i in range(n):
            self.key += self.key[i % len(self.key)]

    def _encrypt_single(self, m, k):
        x = (ord(m) + ord(k)) % 26 + ord("A")
        return chr(x)

    def _decrypt_single(self, m, k):
        x = (ord(m) - ord(k)) % 26 + ord('A')
        return chr(x)

    def encrypt(self) -> str:
        self.preprocess_key()
        cipher_text = ""
        for i in range(len(self.msg)):
            cipher_text += self._encrypt_single(self.msg[i], self.key[i])
        return cipher_text

    def decrypt(self) -> str:
        plain_text = ""
        for i in range(len(self.msg)):
            plain_text += self._decrypt_single(self.msg[i], self.key[i])
        return plain_text


class AutoVigenereCipher(VigenereCipher):
    def preprocess_key(self):
        n = len(self.msg) - len(self.key)
        for i in range(n):
            self.key += self.msg[i % len(self.key)]

    def decrypt(self) -> str:
        k = len(self.key)
        for i in range(len(self.msg)):
            x = self._decrypt_single(self.msg[i], self.key[i])
            self.key += x
        return self.key[k:]


class FullVigenereCipher(VigenereCipher):
    def preprocess_key(self):
        # TODO
        return super().preprocess_key()


class ExtendedVigenereCipher(VigenereCipher):
    allow_byte = True

    def preprocess_key(self):
        # TODO
        return super().preprocess_key()
