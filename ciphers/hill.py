from math import sqrt, floor
from typing import List
import numpy as np
from sympy import Matrix

from ciphers.base import Cipher


def _split(string: str, n: int) -> List[str]:
    return [(string[i:i + n]) for i in range(0, len(string), n)]


class HillCipher(Cipher):
    def preprocess_key(self):
        self.key = list(map(int, self.key.split(",")))
        self.m = floor(sqrt(len(self.key)))
        self.key = self.key[:self.m ** 2]
        self.key = Matrix(np.reshape(self.key, (self.m, self.m)))

    def encrypt_decrypt_helper(self, is_encrypt: bool) -> str:
        self.preprocess_key()
        ret = []
        for char_group in _split(self.msg, self.m):
            char_mat = Matrix(np.array(list(map(lambda c: ord(c) - ord("A"), list(char_group)))))
            cip_mat = (self.key if is_encrypt else self.key.inv_mod(26)) * char_mat
            ret += list(map(lambda x: chr(x % 26 + ord("A")), cip_mat))
        return "".join(ret)

    def encrypt(self) -> str:
        return self.encrypt_decrypt_helper(is_encrypt=True)

    def decrypt(self) -> str:
        return self.encrypt_decrypt_helper(is_encrypt=False)
