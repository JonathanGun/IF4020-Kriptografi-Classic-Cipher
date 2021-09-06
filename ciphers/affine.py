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
    def _encrypt_single(self, p, m, b):
        return chr((m * (ord(p) - ord('A')) + b) % 26 + ord("A"))

    def _decrypt_single(self, c, mod_m, b):
        return chr((mod_m * (ord(c) - ord('A') - b)) % 26 + ord("A"))

    def encrypt(self) -> str:
        m, b = map(int, self.key.split(","))
        ret = [self._encrypt_single(p, m, b) for p in self.msg]
        return "".join(ret)

    def decrypt(self) -> str:
        m, b = map(int, self.key.split(","))
        mod_m = modinv(m, 26)
        ret = [self._decrypt_single(c, mod_m, b) for c in self.msg]
        return "".join(ret)
