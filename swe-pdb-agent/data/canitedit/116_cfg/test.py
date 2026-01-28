from solution import *
import math

def test_all():
    parse_tree1 = ParseTree(["expr", ";"], "stmt")
    parse_tree2 = ParseTree(["expr", ";"], "notsame")
    assert parse_tree1 != parse_tree2
    parse_tree3 = ParseTree(["expr", ";", "b"], "stmt")
    assert parse_tree1 != parse_tree3
    parse_tree4 = ParseTree(["expr", "a"], "stmt")
    assert parse_tree1 != parse_tree4
    assert parse_tree1 != 1
    p = Parser()
    assert p.parse(["expr", ";"]) == ParseTree(["expr", ";"], "stmt")
    assert p.parse(["if", "(", "expr", ")", "expr", ";"]) == ParseTree(
        ["if", "(", "expr", ")", ParseTree(["expr", ";"], "stmt")], "stmt"
    )
    assert p.parse(
        ["if", "(", "expr", ")", "if", "(", "expr", ")", "expr", ";"]
    ) == ParseTree(
        [
            "if",
            "(",
            "expr",
            ")",
            ParseTree(
                ["if", "(", "expr", ")", ParseTree(["expr", ";"], "stmt")], "stmt"
            ),
        ],
        "stmt",
    )
    assert p.parse(["other"]) == ParseTree(["other"], "stmt")

    try:
        p.parse(["expr"])
        assert False
    except Exception:
        assert True

    try:
        p.parse(["other", ";"])
        assert False
    except ValueError:
        assert True

    try:
        p.parse(["expr", "if"])
        assert False
    except ValueError:
        assert True

    try:
        p.parse(["random", ";"])
        assert False
    except ValueError:
        assert True

    assert p.parse(["for", "(", ";", "expr", ";", "expr", ")", "other"]) == ParseTree(
        [
            "for",
            "(",
            ParseTree(["e"], "optexpr"),
            ";",
            ParseTree(["expr"], "optexpr"),
            ";",
            ParseTree(["expr"], "optexpr"),
            ")",
            ParseTree(["other"], "stmt"),
        ],
        "stmt",
    )

    assert p.parse(["for", "(", ";", ";", ")", "other"]) == ParseTree(
        [
            "for",
            "(",
            ParseTree(["e"], "optexpr"),
            ";",
            ParseTree(["e"], "optexpr"),
            ";",
            ParseTree(["e"], "optexpr"),
            ")",
            ParseTree(["other"], "stmt"),
        ],
        "stmt",
    )

    assert p.parse(["for", "(", "expr", ";", ";", ")", "other"]) == ParseTree(
        [
            "for",
            "(",
            ParseTree(["expr"], "optexpr"),
            ";",
            ParseTree(["e"], "optexpr"),
            ";",
            ParseTree(["e"], "optexpr"),
            ")",
            ParseTree(["other"], "stmt"),
        ],
        "stmt",
    )

    assert p.parse(["for", "(", "expr", ";", ";", "expr", ")", "other"]) == ParseTree(
        [
            "for",
            "(",
            ParseTree(["expr"], "optexpr"),
            ";",
            ParseTree(["e"], "optexpr"),
            ";",
            ParseTree(["expr"], "optexpr"),
            ")",
            ParseTree(["other"], "stmt"),
        ],
        "stmt",
    )

    assert p.parse(
        ["for", "(", "expr", ";", ";", "expr", ")", "expr", ";"]
    ) == ParseTree(
        [
            "for",
            "(",
            ParseTree(["expr"], "optexpr"),
            ";",
            ParseTree(["e"], "optexpr"),
            ";",
            ParseTree(["expr"], "optexpr"),
            ")",
            ParseTree(["expr", ";"], "stmt"),
        ],
        "stmt",
    )