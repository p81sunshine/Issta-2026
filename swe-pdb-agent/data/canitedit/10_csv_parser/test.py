from solution import *
import math

def test_all():
        parser = CSVParser('''bim,boom,bam,bap
    duck,duck,goose,duck
    1,0,1,0''')
    
        p2 = CSVParser('''''')
        p3 = CSVParser('''thing''')
        p4 = CSVParser('''thing1, thing2
    a, a''')
        p5 = CSVParser(''',
    ,''')
    
        assert parser.contents() == [["bim", "boom", "bam", "bap"],
                                     ["duck", "duck", "goose", "duck"],
                                     ["1", "0", "1", "0"]]
        assert parser.header() == ["bim", "boom", "bam", "bap"]
        assert p2.contents() == [['']]
        assert p2.header() == ['']
        assert p3.contents() == [['thing']]
        assert p3.header() == ['thing']
        assert p4.contents() == [['thing1', ' thing2'], ['a', ' a']]
        assert p4.header() == ['thing1', ' thing2']
        assert p5.contents() == [['', ''], ['', '']]
        assert p5.header() == ['', '']