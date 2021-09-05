from ciphers.base import Cipher


class EnigmaCipher(Cipher):
    def encrypt(self) -> str:
        # TODO
        return self.msg + "ASD"

    def decrypt(self) -> str:
        # TODO
        return "ASD" + self.msg
