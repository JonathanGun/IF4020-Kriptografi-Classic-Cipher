from ciphers.affine import AffineCipher


def test_sample():
    plaintext = "kripto"
    key = "7, 10"
    ciphertext = AffineCipher(plaintext, key).encrypt()
    expected = "CZOLNE"
    assert ciphertext == expected
