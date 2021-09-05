from ciphers.enigma import EnigmaCipher


def test_sample():
    plaintext = "B"
    key = "24, 26, 1"
    ciphertext = EnigmaCipher(plaintext, key).encrypt()
    expected = "I"
    assert ciphertext == expected
