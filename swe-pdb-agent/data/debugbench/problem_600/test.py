from solution import *

def test_example_1():
    editor = TextEditor()
    assert editor.addText("leetcode") is None
    assert editor.deleteText(4) == 4
    assert editor.addText("practice") is None
    assert editor.cursorRight(3) == "etpractice"
    assert editor.cursorLeft(8) == "leet"
    assert editor.deleteText(10) == 4
    assert editor.cursorLeft(2) == ""
    assert editor.cursorRight(6) == "practi"

def test_cursor_left_on_empty():
    editor = TextEditor()
    result = editor.cursorLeft(1)
    assert result == ""

def test_cursor_right_on_empty():
    editor = TextEditor()
    result = editor.cursorRight(1)
    assert result == ""

def test_cursor_movement():
    editor = TextEditor()
    editor.addText("abc")
    assert editor.cursorLeft(1) == "ab"
    assert editor.cursorRight(1) == "abc"

def test_delete_less_than_available():
    editor = TextEditor()
    editor.addText("abc")
    assert editor.deleteText(5) == 3
    assert editor.cursorLeft(1) == ""