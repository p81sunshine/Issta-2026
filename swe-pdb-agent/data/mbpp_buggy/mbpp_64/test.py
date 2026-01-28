from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_subject_marks_base():
    assert subject_marks([['Social sciences', 82], ['English', 88], ['Science', 90], ['Maths', 97]]) == [['Social sciences', 82], ['English', 88], ['Science', 90], ['Maths', 97]]
    assert subject_marks([['Social', 33], ['Telugu', 49], ['Hindhi', 54]]) == [['Social', 33], ['Telugu', 49], ['Hindhi', 54]]
    assert subject_marks([['Biology', 45], ['Physics', 96], ['Chemistry', 97]]) == [['Biology', 45], ['Physics', 96], ['Chemistry', 97]]
