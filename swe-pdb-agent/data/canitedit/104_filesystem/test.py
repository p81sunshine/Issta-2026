from solution import *
import math

def test_all():
    regular_file = RegularFile("example.txt", 0o644, "user1", "Hello, world!")
    assert regular_file.name == "example.txt"
    assert regular_file.permissions == 0o644
    assert regular_file.owner == "user1"
    assert regular_file.content == "Hello, world!"

    try:
        invalid_file = RegularFile(
            "badfile.txt", 0o1000, "user2", "This should fail")
    except:
        pass
    else:
        assert False, "Expected an AssertionError for invalid permissions"

    assert regular_file.owner == "user1"

    transformed_file = regular_file.map_content(lambda content: content.upper())
    assert transformed_file.content == "HELLO, WORLD!"
    assert transformed_file.name == "example.txt"
    assert transformed_file.permissions == 0o644

    regular_file = RegularFile("example.txt", 0o644, "user1", "Hello, world!")
    regular_file_exp1 = RegularFile(
        "example.txt", 0o644, "user1", "HELLO, WORLD!")

    assert regular_file.map_content(
        lambda content: content.upper()) == regular_file_exp1

    d1 = Directory("user1", 0o700, "user1", [
        regular_file,
        RegularFile("notes.txt", 0o600, "user1", "Some notes"),
        RegularFile("todo.txt", 0o600, "user1", "Some tasks"),
    ])

    d1_exp = Directory("user1", 0o700, "user1", [
        regular_file_exp1,
        RegularFile("notes.txt", 0o600, "user1", "SOME NOTES"),
        RegularFile("todo.txt", 0o600, "user1", "SOME TASKS"),
    ])

    assert d1.map_content(lambda content: content.upper()) == d1_exp

    d2 = Directory("user2", 0o700, "user2", [
        d1,
        RegularFile("stuff.txt", 0o600, "user2", "Some stuff"),
    ])

    d2_exp = Directory("user2", 0o700, "user2", [
        d1_exp,
        RegularFile("stuff.txt", 0o600, "user2", "SOME STUFF"),
    ])

    assert d2.map_content(lambda content: content.upper()) == d2_exp

    fs = Directory("root", 0o755, "user1", [
        Directory("home", 0o755, "user1", [
            d2,
        ]),
    ])

    fs_exp = Directory("root", 0o755, "user1", [
        Directory("home", 0o755, "user1", [
            d2_exp,
        ]),
    ])

    assert fs.map_content(lambda content: content.upper()) == fs_exp

    regular_file_exp2 = RegularFile(
        "EXAMPLE.TXT", 0o644, "user1", "Hello, world!")

    def upper_name(file: File):
        file.name = file.name.upper()

    new_regular_file = RegularFile("example.txt", 0o644, "user1", "Hello, world!")
    new_regular_file.map_files(upper_name)
    assert new_regular_file == regular_file_exp2

    new_d1 = Directory("user1", 0o700, "user1", [
        new_regular_file,
        RegularFile("notes.txt", 0o600, "user1", "Some notes"),
        RegularFile("todo.txt", 0o600, "user1", "Some tasks"),
    ])

    new_d1_exp = Directory("USER1", 0o700, "user1", [
        regular_file_exp2,
        RegularFile("NOTES.TXT", 0o600, "user1", "Some notes"),
        RegularFile("TODO.TXT", 0o600, "user1", "Some tasks"),
    ])

    new_d1.map_files(upper_name)
    assert new_d1 == new_d1_exp

    new_d2 = Directory("user2", 0o700, "user2", [
        Directory("home", 0o755, "user2", [
            Directory("user1", 0o700, "user1", [
                new_regular_file,
                RegularFile("notes.txt", 0o600, "user1", "Some notes"),
                RegularFile("todo.txt", 0o600, "user1", "Some tasks"),
            ]),
        ]),
        RegularFile("stuff.txt", 0o600, "user2", "Some stuff"),
    ])

    new_d2_exp = Directory("USER2", 0o700, "user2", [
        Directory("HOME", 0o755, "user2", [
            Directory("USER1", 0o700, "user1", [
                regular_file_exp2,
                RegularFile("NOTES.TXT", 0o600, "user1", "Some notes"),
                RegularFile("TODO.TXT", 0o600, "user1", "Some tasks"),
            ]),
        ]),
        RegularFile("STUFF.TXT", 0o600, "user2", "Some stuff"),
    ])

    new_d2.map_files(upper_name)
    assert new_d2 == new_d2_exp