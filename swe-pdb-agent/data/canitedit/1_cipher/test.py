from solution import *
import math

def test_all():
    cipher = Cipher()

    default = cipher.ciphers["default"]

    assert default['m'] == 'l'
    assert default['n'] == 'o'
    assert default['d'] == 'd'
    assert default['w'] == 'v'

    assert cipher.translate("default", "willthedogsbark") == "vhmmuicdnfrabsj"
    assert cipher.translate("default", "pqpqpq") == "qpqpqp"

    cipher.caesar_cipher(0)
    caesar1 = cipher.ciphers["caesar0"]

    assert caesar1['a'] == 'a'
    assert caesar1['m'] == 'm'
    assert caesar1['n'] == 'n'

    cipher.caesar_cipher(30)
    caesar30 = cipher.ciphers["caesar30"]

    assert caesar30['a'] == 'e'
    assert caesar30['y'] == 'c'

    cipher.caesar_cipher(5)
    caesar5 = cipher.ciphers["caesar5"]
    assert caesar5['a'] == 'f'
    assert caesar5['z'] == 'e'

    assert len(cipher.ciphers) == 4

    # add a cipher
    cipher.add_cipher("test", {'a': 'b', 'b': 'a'})
    assert cipher.ciphers["test"]['a'] == 'b'
    assert cipher.ciphers["test"]['b'] == 'a'