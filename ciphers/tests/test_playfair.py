from ciphers.playfair import PlayfairCipher


def test_sample():
    plaintext = "temui ibu nanti malam"
    key = "jalan ganesha sepuluh"
    ciphertext = PlayfairCipher(plaintext, key).encrypt()
    expected = "ZBRSFYKUPGLGRKVSNLQV"
    assert ciphertext == expected
