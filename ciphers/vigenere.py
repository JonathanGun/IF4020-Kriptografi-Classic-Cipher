from ciphers.base import Cipher


class VigenereCipher(Cipher):
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
    allow_byte = True

    def encrypt(msg: str) -> str:
        # TODO
        return msg + "ASDdsa1"

    def decrypt(msg: str) -> str:
        # TODO
        return "1dsaASD" + msg
