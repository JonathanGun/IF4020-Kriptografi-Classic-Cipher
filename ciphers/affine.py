from ciphers.base import Cipher


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


class AffineCipher(Cipher):
    def encrypt(self) -> str:
        m, b = map(int, self.key.split(","))
        ret = []
        for p in self.msg:
            c = (m * (ord(p) - ord('A')) + b) % 26
            c = chr(c + ord('A'))
            ret.append(c)
        return "".join(ret)

    def decrypt(self) -> str:
        m, b = map(int, self.key.split(","))
        mod_m = modinv(m, 26)

        ret = []
        for c in self.msg:
            p = (mod_m * (ord(c) - ord('A') - b)) % 26
            p = chr(p + ord('A'))
            ret.append(p)
        return "".join(ret)
