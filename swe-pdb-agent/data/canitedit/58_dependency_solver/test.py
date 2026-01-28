from solution import *
import math

# foo has no dependencies

def test_all():
    foo = Package(
        "foo",
        [
            PackageVersion(Semver(0, 0, 1)),
            PackageVersion(Semver(1, 0, 0)),
            PackageVersion(Semver(1, 1, 0)),
            PackageVersion(Semver(1, 2, 3)),
            PackageVersion(Semver(1, 2, 4)),
            PackageVersion(Semver(1, 2, 5)),
            PackageVersion(Semver(2, 0, 0)),
        ],
    )

    # bar depends on foo, only after version 1.0.0
    foo_constraint1 = SemverConstraint("foo", ">=", Semver(1, 0, 0))
    foo_constraint2 = SemverConstraint("foo", "<", Semver(2, 0, 0))
    bar = Package(
        "bar",
        [
            PackageVersion(Semver(0, 0, 1)),
            PackageVersion(Semver(0, 2, 1)),
            PackageVersion(Semver(1, 0, 0), [foo_constraint1]),
            PackageVersion(Semver(1, 1, 0), [foo_constraint1]),
            PackageVersion(Semver(1, 2, 0), [foo_constraint1]),
            PackageVersion(Semver(2, 0, 0), [foo_constraint2]),
        ],
    )

    # baz depends on bar and also foo (but only after version 1.2.3)
    foo_constraint3 = SemverConstraint("foo", ">=", Semver(1, 2, 3))
    bar_constraint = SemverConstraint("bar", "==", Semver(2, 0, 0))
    baz = Package(
        "baz",
        [
            PackageVersion(Semver(0, 0, 1)),
            PackageVersion(Semver(0, 2, 1), [bar_constraint]),
            PackageVersion(Semver(1, 0, 0), [bar_constraint]),
            PackageVersion(Semver(1, 1, 0), [bar_constraint]),
            PackageVersion(Semver(1, 2, 0), [bar_constraint]),
            PackageVersion(Semver(1, 2, 3), [bar_constraint, foo_constraint3]),
            PackageVersion(Semver(1, 2, 4), [bar_constraint]),
        ]
    )

    # boo depends on baz, at wildly different versions
    baz_constraint1 = SemverConstraint("baz", "==", Semver(0, 0, 1))
    baz_constraint2 = SemverConstraint("baz", "<", Semver(1, 0, 0))
    baz_constraint3 = SemverConstraint("baz", ">", Semver(1, 0, 0))
    baz_constraint4 = SemverConstraint("baz", "<=", Semver(1, 2, 3))

    boo = Package(
        "boo",
        [
            PackageVersion(Semver(0, 0, 1), [baz_constraint1]),
            PackageVersion(Semver(0, 2, 1), [baz_constraint1]),
            PackageVersion(Semver(1, 0, 0), [baz_constraint2]),
            PackageVersion(Semver(1, 1, 0), [baz_constraint2]),
            PackageVersion(Semver(1, 2, 0), [baz_constraint2]),
            PackageVersion(Semver(1, 2, 3), [baz_constraint3]),
            PackageVersion(Semver(1, 2, 4), [baz_constraint3]),
            PackageVersion(Semver(1, 2, 5), [baz_constraint3]),
            PackageVersion(Semver(2, 0, 0), [baz_constraint4]),
        ]
    )

    # WORLD is a list of all packages
    WORLD = [
        foo,
        bar,
        baz,
        boo,
    ]

    assert Semver(1, 2, 3) == Semver(1, 2, 3)
    assert Semver(1, 2, 3) != Semver(1, 2, 4)
    assert Semver(1, 2, 3) < Semver(1, 2, 4)
    assert Semver(1, 2, 3) <= Semver(1, 2, 4)
    assert Semver(1, 2, 3) <= Semver(1, 2, 3)
    assert Semver(1, 2, 4) > Semver(1, 2, 3)
    assert not (Semver(1, 2, 3) > Semver(1, 2, 4))
    assert not (Semver(1, 2, 3) < Semver(1, 2, 3))
    assert not (Semver(1, 2, 3) > Semver(1, 2, 3))
    assert not (Semver(1, 2, 3) < Semver(1, 0, 0))
    assert Semver(2, 2, 3) > Semver(1, 2, 4)
    assert Semver(3, 2, 3) < Semver(4, 2, 3)
    assert Semver(3, 2, 3) < Semver(4, 2, 3)
    assert Semver(3, 2, 3) < Semver(3, 4, 3)
    assert Semver(1, 2, 4) >= Semver(1, 2, 3)
    assert Semver(1, 2, 4) >= Semver(1, 2, 4)
    assert Semver(1, 3, 4) > Semver(1, 2, 4)

    # hashable
    assert hash(Semver(1, 2, 3)) == hash(Semver(1, 2, 3))
    assert hash(Semver(1, 2, 3)) != hash(Semver(1, 2, 4))

    sem = Semver(1, 2, 3)
    constraint = SemverConstraint("foo", "==", sem)
    assert constraint.satisfies(Semver(1, 2, 3))
    assert not constraint.satisfies(Semver(1, 2, 4))

    constraint = SemverConstraint("foo", ">=", sem)
    assert constraint.satisfies(Semver(1, 2, 3))
    assert constraint.satisfies(Semver(1, 2, 4))
    assert not constraint.satisfies(Semver(1, 2, 2))

    constraint = SemverConstraint("foo", "<=", sem)
    assert constraint.satisfies(Semver(1, 2, 3))
    assert constraint.satisfies(Semver(1, 2, 2))
    assert not constraint.satisfies(Semver(1, 2, 4))

    constraint = SemverConstraint("foo", ">", sem)
    assert constraint.satisfies(Semver(1, 2, 4))
    assert not constraint.satisfies(Semver(1, 2, 3))
    assert not constraint.satisfies(Semver(1, 2, 2))

    constraint = SemverConstraint("foo", "<", sem)
    assert constraint.satisfies(Semver(1, 2, 2))
    assert not constraint.satisfies(Semver(1, 2, 3))
    assert not constraint.satisfies(Semver(1, 2, 4))

    max1 = foo.max_satisfying_version(
        [SemverConstraint("foo", "==", Semver(1, 2, 3))])
    assert max1
    assert max1.version == Semver(1, 2, 3)
    max2 = foo.max_satisfying_version(
        [SemverConstraint("foo", ">=", Semver(1, 2, 3))])
    assert max2
    assert max2.version == Semver(2, 0, 0)

    max1 = bar.max_satisfying_version(
        [SemverConstraint("foo", "==", Semver(3, 2, 3))])
    assert max1 is None

    # dup dep
    try:
        PackageVersion(Semver(0, 0, 1), [
            baz_constraint1, baz_constraint1])
    except:
        pass
    else:
        assert False

    # dup dep 2
    try:
        PackageVersion(Semver(0, 0, 1), [
                       baz_constraint1, baz_constraint2, baz_constraint1])
    except:
        pass
    else:
        assert False

    # dup dep 3
    try:
        PackageVersion(Semver(0, 0, 1), [
            foo_constraint1, foo_constraint2, foo_constraint1])
    except:
        pass
    else:
        assert False

    # dup dep 4
    try:
        PackageVersion(Semver(0, 0, 1), [
            foo_constraint1, foo_constraint2])
    except:
        pass
    else:
        assert False

    # dup version
    try:
        Package(
            "dup",
            [
                PackageVersion(Semver(0, 0, 1)),
                PackageVersion(Semver(0, 0, 1)),
            ]
        )
    except:
        pass
    else:
        assert False

    # dup version 2
    try:
        Package(
            "dup",
            [
                PackageVersion(Semver(0, 0, 1)),
                PackageVersion(Semver(1, 0, 0)),
                PackageVersion(Semver(0, 0, 1)),
            ]
        )
    except:
        pass
    else:
        assert False

    # dup version 3
    try:
        Package(
            "dup",
            [
                PackageVersion(Semver(0, 0, 1)),
                PackageVersion(Semver(1, 0, 0)),
                PackageVersion(Semver(1, 0, 0)),
            ]
        )
    except:
        pass
    else:
        assert False

    # dup version 4
    try:
        Package(
            "dup",
            [
                PackageVersion(Semver(0, 0, 1)),
                PackageVersion(Semver(1, 2, 0)),
                PackageVersion(Semver(1, 0, 3)),
                PackageVersion(Semver(1, 0, 1)),
                PackageVersion(Semver(1, 2, 0)),
            ]
        )
    except:
        pass
    else:
        assert False