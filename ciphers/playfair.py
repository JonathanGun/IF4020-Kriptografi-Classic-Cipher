import re
from typing import List
from ciphers.base import Cipher


def _split(string: str, n: int = 2) -> List[str]:
    return [(string[i:i + n]) for i in range(0, len(string), n)]


def _translate_coord_cyclic(r, c, dr, dc):
    return (r + dr) % 5, (c + dc) % 5


class PlayfairCipher(Cipher):
    REMOVED_CHAR = "J"
    REPLACE_CHAR = "I"

    def __init__(self, msg: str, key: str):
        super().__init__(msg, key)
        self.key, self.key_dict = self.Key(self.key, self.REMOVED_CHAR).preprocess()
        self.msg = self.msg.replace(self.REMOVED_CHAR, self.REPLACE_CHAR)
        self.list_msg = self.__split_and_insert(self.msg, 'X')

    def __split_and_insert(self, msg: str, ins_char: str = 'X') -> List[str]:
        ret = []
        cur = ''
        last = ''
        for c in msg:
            if c == last:
                cur += ins_char
            if len(cur) == 2:
                ret.append(cur)
                cur = ''
            cur += c
            if len(cur) == 2:
                ret.append(cur)
                cur = ''
            last = c
        if cur:
            ret.append(cur + ins_char)
        return ret

    class Key:
        def __init__(self, key: str, removed_char: str):
            self.key = key
            self.removed_char = removed_char

        def preprocess(self):
            self.remove_leftover_char().remove_whitespaces().remove_duplicates().prepend_key().to_square()
            self.key_dict = self.to_dict()
            return (self.key, self.key_dict)

        def remove_whitespaces(self):
            self.key = re.sub(r"\s+", '', self.key)
            return self

        def remove_leftover_char(self):
            self.key = self.key.replace(self.removed_char, "")
            return self

        def to_square(self) -> List[str]:
            self.key = _split(self.key, 5)
            return self

        def remove_duplicates(self) -> str:
            ret = ""
            for c in self.key:
                if c not in ret:
                    ret += c
            self.key = ret
            return self

        def prepend_key(self) -> str:
            ret = self.key
            for i in range(26):
                c = chr(ord("A") + i)
                if c == self.removed_char:
                    continue
                if c not in ret:
                    ret += c
            self.key = ret
            return self

        def to_dict(self):
            ret = {}
            for i, line in enumerate(self.key):
                for j, c in enumerate(line):
                    ret[c] = (i, j)
            return ret

    def encrypt(self) -> str:
        self.list_cip = []
        for pair in self.list_msg:
            r1, c1 = self.key_dict[pair[0]]
            r2, c2 = self.key_dict[pair[1]]
            dr1, dc1 = 0, 0
            dr2, dc2 = 0, 0
            if r1 == r2:
                dc1, dc2 = 1, 1
            elif c1 == c2:
                dr1, dr2 = 1, 1
            else:
                dc1, dc2 = c2 - c1, c1 - c2
            cip1_r, cip1_c = _translate_coord_cyclic(r1, c1, dr1, dc1)
            cip2_r, cip2_c = _translate_coord_cyclic(r2, c2, dr2, dc2)
            cip1, cip2 = self.key[cip1_r][cip1_c], self.key[cip2_r][cip2_c]
            self.list_cip.append(cip1 + cip2)
        return "".join(self.list_cip)

    def decrypt(self) -> str:
        self.list_cip = []
        for pair in self.list_msg:
            r1, c1 = self.key_dict[pair[0]]
            r2, c2 = self.key_dict[pair[1]]
            dr1, dc1 = 0, 0
            dr2, dc2 = 0, 0
            if r1 == r2:
                dc1, dc2 = -1, -1
            elif c1 == c2:
                dr1, dr2 = -1, -1
            else:
                dc1, dc2 = c2 - c1, c1 - c2
            cip1_r, cip1_c = _translate_coord_cyclic(r1, c1, dr1, dc1)
            cip2_r, cip2_c = _translate_coord_cyclic(r2, c2, dr2, dc2)
            cip1, cip2 = self.key[cip1_r][cip1_c], self.key[cip2_r][cip2_c]
            self.list_cip.append(cip1 + cip2)
        return "".join(self.list_cip)
