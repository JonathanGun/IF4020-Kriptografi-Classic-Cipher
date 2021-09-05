import re
from typing import List
from ciphers.base import Cipher


class PlayfairCipher(Cipher):
    REMOVED_CHAR = "J"
    REPLACE_CHAR = "I"

    def _split(string: str, n: int = 2) -> List[str]:
        return [(string[i:i + n]) for i in range(0, len(string), n)]

    def to_square(key: str) -> List[str]:
        return PlayfairCipher._split(key, 5)

    def remove_duplicates(key: str) -> str:
        ret = ""
        for c in key:
            if c not in ret:
                ret += c
        return ret

    def prepend_key(key: str) -> str:
        for i in range(26):
            c = chr(ord("A") + i)
            if c == PlayfairCipher.REMOVED_CHAR:
                continue
            if c not in key:
                key += c
        return key

    def to_dict(key: List[str]):
        ret = {}
        for i, line in enumerate(key):
            for j, c in enumerate(line):
                ret[c] = (i, j)
        return ret

    def split_and_insert(msg: str, ins_char: str = 'X') -> List[str]:
        ret = []
        cur = ''
        for c in msg:
            if c == cur:
                ret.append(cur + ins_char)
                cur = c
            elif len(cur) == 1:
                ret.append(cur + c)
                cur = ''
            else:
                cur = c
        if cur:
            ret.append(cur + ins_char)
        return ret

    def preprocess_key(key: str) -> List[str]:
        key = key.replace(PlayfairCipher.REMOVED_CHAR, "")
        key = re.sub(r"\s+", '', key)
        key = PlayfairCipher.remove_duplicates(key)
        key = PlayfairCipher.prepend_key(key)
        key = PlayfairCipher.to_square(key)
        key_dict = PlayfairCipher.to_dict(key)
        return (key, key_dict)

    def preprocess_msg(msg: str, n: int = 2) -> List[str]:
        msg = msg.replace(PlayfairCipher.REMOVED_CHAR, PlayfairCipher.REPLACE_CHAR)
        msg = PlayfairCipher.split_and_insert(msg, 'X')
        return msg

    def _translate_coord_cyclic(r, c, dr, dc):
        return (r + dr) % 5, (c + dc) % 5

    def _encrypt(list_msg: List[str], key: str) -> str:
        key, key_dict = key
        list_cip = []
        for pair in list_msg:
            r1, c1 = key_dict[pair[0]]
            r2, c2 = key_dict[pair[1]]
            dr1, dc1 = 0, 0
            dr2, dc2 = 0, 0
            if r1 == r2:
                dc1, dc2 = 1, 1
            elif c1 == c2:
                dr1, dr2 = 1, 1
            else:
                dc1, dc2 = c1 - c2, c1 - c2
            cip1_r, cip1_c = PlayfairCipher._translate_coord_cyclic(r1, c1, dr1, dc1)
            cip2_r, cip2_c = PlayfairCipher._translate_coord_cyclic(r2, c2, dr2, dc2)
            cip1 = key[cip1_r][cip1_c]
            cip2 = key[cip2_r][cip2_c]
            list_cip.append(cip1 + cip2)
        return "".join(list_cip)

    def _decrypt(list_msg: List[str], key: str) -> str:
        key, key_dict = key
        list_cip = []
        for pair in list_msg:
            r1, c1 = key_dict[pair[0]]
            r2, c2 = key_dict[pair[1]]
            dr1, dc1 = 0, 0
            dr2, dc2 = 0, 0
            if r1 == r2:
                dc1, dc2 = -1, -1
            elif c1 == c2:
                dr1, dr2 = -1, -1
            else:
                dc1, dc2 = c2 - c1, c1 - c2
            print(dr1, dc1, dr2, dc2)
            cip1_r, cip1_c = PlayfairCipher._translate_coord_cyclic(r1, c1, dr1, dc1)
            cip2_r, cip2_c = PlayfairCipher._translate_coord_cyclic(r2, c2, dr2, dc2)
            cip1 = key[cip1_r][cip1_c]
            cip2 = key[cip2_r][cip2_c]
            list_cip.append(cip1 + cip2)
        return "".join(list_cip)

    def encrypt(msg: str, key: str) -> str:
        key = PlayfairCipher.preprocess_key(key)
        list_msg = PlayfairCipher.preprocess_msg(msg)
        ret = PlayfairCipher._encrypt(list_msg, key)
        return ret

    def decrypt(msg: str, key: str) -> str:
        key = PlayfairCipher.preprocess_key(key)
        list_msg = PlayfairCipher._split(msg, 2)
        ret = PlayfairCipher._decrypt(list_msg, key)
        return ret
