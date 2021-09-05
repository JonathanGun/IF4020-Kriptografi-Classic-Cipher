import re
from abc import ABC, abstractmethod


class Cipher(ABC):
    allow_byte = False

    def __init__(self, msg: str, key: str):
        self.msg = re.sub('[^A-Z]+', '', msg.upper())
        self.key = key.upper()

    @abstractmethod
    def encrypt(self) -> str:
        pass

    @abstractmethod
    def decrypt(self) -> str:
        pass
