from ciphers.base import Cipher


class AffineCipher(Cipher):
    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = AffineCipher.egcd(b % a, a)
            return (g, x - (b // a) * y, y)

    def modinv(a, m):
        g, x, y = AffineCipher.egcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m

    def encrypt(msg: str, key: str) -> str:
        m, b = map(int, key.split(","))
        ret = []
        for p in msg:
            c = (m * (ord(p) - ord('A')) + b) % 26
            c = chr(c + ord('A'))
            ret.append(c)
        return "".join(ret)

    def decrypt(msg: str, key: str) -> str:
        m, b = map(int, key.split(","))
        mod_m = AffineCipher.modinv(m, 26)

        ret = []
        for c in msg:
            p = (mod_m * (ord(c) - ord('A') - b)) % 26
            p = chr(p + ord('A'))
            ret.append(p)
        return "".join(ret)
