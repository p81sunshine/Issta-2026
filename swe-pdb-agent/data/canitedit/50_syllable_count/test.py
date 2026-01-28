from solution import *
import math

def test_all():
    assert syllable_count('italiam fato profugus laviniaque venit') == 17
    assert syllable_count('ante mare et terras et quod tegit omnia caelum') == 17
    assert syllable_count('repostum iudicium') == 7
    assert syllable_count('mollia cum duris sine pondere habentia pondus') == 16
    assert syllable_count('') == 0
    assert syllable_count('sam henry') == 2