from solution import *

def test_example_1():
    import solution
    solution.stack = []
    solution.q = deque()
    addText("leetcode")
    assert deleteText(4) == 4
    addText("practice")
    assert cursorRight(3) == "etpractice"
    assert cursorLeft(8) == "leet"
    assert deleteText(10) == 4
    assert cursorLeft(2) == ""
    assert cursorRight(6) == "practi"

def test_cursor_moves():
    import solution
    solution.stack = []
    solution.q = deque()
    addText("abc")
    assert cursorLeft(10) == ""
    assert cursorRight(10) == "abc"

def test_delete_more_than_present():
    import solution
    solution.stack = []
    solution.q = deque()
    addText("hi")
    assert deleteText(10) == 2
    assert cursorLeft(10) == ""

def test_empty_text():
    import solution
    solution.stack = []
    solution.q = deque()
    assert deleteText(1) == 0
    assert cursorLeft(1) == ""
    assert cursorRight(1) == ""

def test_cursor_and_10_chars():
    import solution
    solution.stack = []
    solution.q = deque()
    addText("1234567890")
    assert cursorLeft(5) == "12345"
    assert cursorRight(5) == "1234567890"
    assert cursorLeft(10) == ""
    assert cursorRight(10) == "1234567890"