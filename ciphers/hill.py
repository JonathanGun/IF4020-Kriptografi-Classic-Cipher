from ciphers.base import Cipher


class HillCipher(Cipher):
    def encrypt(msg: str, key: str) -> str:
        # TODO
        return msg + "ASD"

    def decrypt(msg: str, key: str) -> str:
        # TODO
        return "ASD" + msg
