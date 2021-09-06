from ciphers.hill import HillCipher


def test_sample():
    plaintext = "paymoremoney"
    key = "17, 17, 5, 21, 18, 21, 2, 2, 19"
    ciphertext = HillCipher(plaintext, key).encrypt()
    expected = "LNSHDLEWMTRW"
    assert ciphertext == expected
    # assert HillCipher(expected, key).decrypt() == plaintext.upper()
