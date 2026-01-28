from solution import *

import math

from solution import *

import math

from solution import *

import math

from solution import FileSystem, execute_commands

def test_mkdir():
    fs = FileSystem()
    fs.mkdir('/a/b')
    assert 'a' in fs.fs['/']
    assert 'b' in fs.fs['/']['a']

def test_touch():
    fs = FileSystem()
    fs.touch('/a/b/file.txt')
    assert 'a' in fs.fs['/']
    assert 'b' in fs.fs['/']['a']
    assert 'file.txt' in fs.fs['/']['a']['b']

def test_ls_directory():
    fs = FileSystem()
    fs.mkdir('/a')
    fs.touch('/a/file1.txt')
    fs.touch('/a/file2.txt')
    assert fs.ls('/a') == ['file1.txt', 'file2.txt']

def test_ls_file():
    fs = FileSystem()
    fs.touch('/a/file.txt')
    assert fs.ls('/a/file.txt') == ['file.txt']

def test_execute_commands():
    commands = [
        "mkdir /a/b/c",
        "touch /a/b/d.txt",
        "ls /a/b",
        "touch /a/b/c/e.txt",
        "ls /a/b/c",
        "ls /a"
    ]
    expected_output = [
        "c d.txt",
        "e.txt",
        "b"
    ]
    assert execute_commands(commands) == expected_output