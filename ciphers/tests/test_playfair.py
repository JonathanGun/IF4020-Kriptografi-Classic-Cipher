from ciphers.playfair import PlayfairCipher


def test_simple():
    plaintext = "temui ibu nanti malam"
    key = "jalan ganesha sepuluh"
    ciphertext = PlayfairCipher.encrypt(plaintext, key)
    expected = "ZBRSFYKUPGLGRKVSNLQV"
    assert ciphertext == expected
