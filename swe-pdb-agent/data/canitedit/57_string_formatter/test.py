from solution import *
import math

def test_all():
    assert concatenate_nums("the cat  chased  the mouse") == "the mouse  chased  the cat"
    assert concatenate_nums('Bob  says  "hi"') == '"hi"  says  Bob'

    assert format_string('Bob', 'Suzy', 'the cat  chased  the mouse') == 'Hello, Bob! You have a message from Suzy. The message is: the mouse  chased  the cat'
    assert format_string('adDHksnd', 'ALJdaH', 'Bob  says  "hi"') == 'Hello, Addhksnd! You have a message from Aljdah. The message is: "hi"  says  Bob'
    assert format_string('the cat', 'the mouse', 'the cat  chased  the mouse') == 'Hello, The cat! You have a message from The mouse. The message is: the mouse  chased  the cat'