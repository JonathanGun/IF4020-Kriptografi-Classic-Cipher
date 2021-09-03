from ciphers.base import Cipher


class HillCipher(Cipher):
    def encrypt(msg: str) -> str:
        # TODO
        return msg + "ASD"

    def decrypt(msg: str) -> str:
        # TODO
        return "ASD" + msg
