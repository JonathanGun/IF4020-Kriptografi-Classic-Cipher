from ciphers.vigenere import VigenereCipher, FullVigenereCipher, AutoVigenereCipher, ExtendedVigenereCipher
from ciphers.affine import AffineCipher
from ciphers.hill import HillCipher
from ciphers.enigma import EnigmaCipher
from ciphers.playfair import PlayfairCipher

ciphers = {
    "Vigenere Cipher": VigenereCipher,
    "Full Vigenere Cipher": FullVigenereCipher,
    "Auto Vigenere Cipher": AutoVigenereCipher,
    "Extended Vigenere Cipher": ExtendedVigenereCipher,
    "Affine Cipher": AffineCipher,
    "Hill Cipher": HillCipher,
    "Enigma Cipher": EnigmaCipher,
    "Playfair Cipher": PlayfairCipher,
}


def test_decrypt_encrypt():
    plaintext = "temui ibu nanti malam"
    key = ""
    key_default = "jalan ganesha sepuluh"
    key_affine = "7, 10"
    for cipher in ciphers.values():
        key = key_affine if cipher == AffineCipher else key_default
        print(cipher)
        print("p1:", plaintext)

        ciphertext = cipher(plaintext, key).encrypt()
        if cipher.allow_byte:
            ciphertext = cipher.byte_to_str(ciphertext)
        print("c1:", ciphertext)

        plaintext2 = cipher(ciphertext, key).decrypt()
        if cipher.allow_byte:
            plaintext2 = cipher.byte_to_str(plaintext2)
        print("p2:", plaintext2)

        ciphertext2 = cipher(plaintext2, key).encrypt()
        if cipher.allow_byte:
            ciphertext2 = cipher.byte_to_str(ciphertext2)
        print("c2:", ciphertext2)

        plaintext3 = cipher(ciphertext2, key).decrypt()
        if cipher.allow_byte:
            plaintext3 = cipher.byte_to_str(plaintext3)
        print("p3:", plaintext3)

        assert plaintext2 == plaintext3
