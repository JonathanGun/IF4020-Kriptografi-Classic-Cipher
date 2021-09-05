from ciphers.vigenere import VigenereCipher, AutoVigenereCipher


def test_sample():
    plaintext = "thisplaintext"
    key = "sony"
    ciphertext = VigenereCipher(plaintext, key).encrypt()
    expected = "LVVQHZNGFHRVL"
    assert ciphertext == expected


def test_auto():
    plaintext = "negara penghasil minya"
    key = "indo"
    ciphertext = AutoVigenereCipher(plaintext, key).encrypt()
    expected = "VRJOEEVEEGWEFOSMAVJM"
    assert ciphertext == expected
