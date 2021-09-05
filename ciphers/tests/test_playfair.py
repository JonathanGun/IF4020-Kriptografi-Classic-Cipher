from ciphers.playfair import PlayfairCipher


def test_simple():
    plaintext = "TEMUIIBUNANTIMALAM"
    key = "JALAN GANESHA SEPULUH"
    ciphertext = PlayfairCipher.encrypt(plaintext, key)
    expected = "ZBRSFYKUPGLGRKVSNLQV"
    assert ciphertext == expected
