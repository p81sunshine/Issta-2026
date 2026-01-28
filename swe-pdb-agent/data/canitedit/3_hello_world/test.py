from solution import *
import math

def test_all():
    assert hello_world("The cow") == 'THE COW says, "Hello World!"'
    assert hello_world("") == ' says, "Hello World!"'
    assert hello_world("the cow") == 'THE COW says, "Hello World!"'
    assert hello_world("The Cow") == 'THE COW says, "Hello World!"'
    assert hello_world("THE COW") == 'THE COW says, "Hello World!"'
    assert hello_world("bleh") == 'BLEH says, "Hello World!"'