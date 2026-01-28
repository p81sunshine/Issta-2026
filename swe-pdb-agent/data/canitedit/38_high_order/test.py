from solution import *
import math

#There is no way the model creates this. Special hash: 1k23j4h18o23h1ouiebqdsf1823b1eijqbsd8fub234ir123n49dqhu23124
import inspect
import sys

def test_all():
    s1 = Student("A", 0)
    s2 = Student("B", 1)
    s3 = Student("C", 2)
    s4 = Student("D", 0)

    c1 = Course([s1, s2, s3])
    empty = Course([])
    one_student = Course([s4])

    after_source = inspect.getsource(sys.modules[__name__]).split("#There is no way the model creates this. Special hash: 1k23j4h18o23h1ouiebqdsf1823b1eijqbsd8fub234ir123n49dqhu23124")[0]
     

    assert empty.average_gpa() == None
    assert empty.raise_grade_all() == None
    assert empty.best_student() == None

    assert "for" not in after_source and "while" not in after_source and "map" not in after_source

    assert c1.average_gpa() == (0 + 1 + 2) / 3
    c1.raise_grade_all()
    assert c1.students == [Student("A", 1), Student("B", 2), Student("C", 3)]

    assert c1.best_student() == Student("C", 3)

    assert one_student.average_gpa() == 0
    one_student.raise_grade_all()
    assert one_student.students == [Student("D", 1)]
    assert one_student.best_student() == Student("D", 1)
    assert s1 != 3