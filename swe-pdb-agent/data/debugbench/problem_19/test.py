from solution import *

def test_example_1():
    editor = TextEditor()
    editor.addText("leetcode")
    assert editor.deleteText(4) == 4, "Should delete 4 characters from 'leetcode'"
    editor.addText("practice")
    assert editor.cursorRight(3) == "etpractice", "Cursor right should return 'etpractice'"
    assert editor.cursorLeft(8) == "leet", "Cursor left should return 'leet'"
    assert editor.deleteText(10) == 4, "Should delete 4 characters from 'leetpractice'"
    assert editor.cursorLeft(2) == "", "Cursor left on empty left side should return empty string"
    assert editor.cursorRight(6) == "practi", "Cursor right should return 'practi'"

def test_add_and_delete():
    editor = TextEditor()
    editor.addText("abc")
    assert editor.deleteText(2) == 2, "Should delete 2 characters from 'abc'"
    assert editor.deleteText(10) == 1, "Should delete remaining 1 character"
    editor.addText("xyz")
    assert editor.deleteText(5) == 3, "Should delete all 3 characters of 'xyz'"

def test_cursor_movement():
    editor = TextEditor()
    editor.addText("hello")
    assert editor.cursorLeft(2) == "hel", "Cursor left should return 'hel'"
    assert editor.cursorRight(1) == "hell", "Cursor right should return 'hell'"

def test_delete_empty():
    editor = TextEditor()
    assert editor.deleteText(5) == 0, "Deleting from empty editor should return 0"