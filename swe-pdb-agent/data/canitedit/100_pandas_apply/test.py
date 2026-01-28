from solution import *
import math

def test_all():
    assert StringOperations.remove_duplicates('hello') == 'helo'
    assert StringOperations.remove_duplicates('mississippi') == 'misp'
    assert StringOperations.remove_duplicates('python') == 'python'
    assert StringOperations.remove_duplicates('unique characters') == 'uniqe charts'

    assert StringOperations.word_reversal('Hello. How are you?') == 'you? are How Hello.'
    assert StringOperations.word_reversal('This is a test.') == 'test. a is This'
    assert StringOperations.word_reversal('unique characters') == 'characters unique'
    assert StringOperations.word_reversal('') == ''

    assert StringOperations.remove_vowels('hello') == 'hll'
    assert StringOperations.remove_vowels('world') == 'wrld'
    assert StringOperations.remove_vowels('aeiou') == ''
    assert StringOperations.remove_vowels('') == ''

    assert calculate_all_properties("this is the pandas application problem", [StringOperations.remove_vowels, StringOperations.word_reversal, StringOperations.remove_duplicates]) == ['ths s th pnds pplctn prblm', 'problem application pandas the is this', 'this epandlcorbm']
    assert calculate_all_properties("Lorem ipsum dolor sit amet consectetur adipiscing elit", [StringOperations.remove_vowels, StringOperations.word_reversal, StringOperations.remove_duplicates]) == ['Lrm psm dlr st mt cnscttr dpscng lt', 'elit adipiscing consectetur amet sit dolor ipsum Lorem', 'Lorem ipsudltacng']
    assert calculate_all_properties("reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla", [StringOperations.remove_vowels, StringOperations.word_reversal, StringOperations.remove_duplicates]) == ['rprhndrt n vlptt vlt ss cllm dlr  fgt nll', 'nulla fugiat eu dolore cillum esse velit voluptate in reprehenderit', 'rephndit voluascmfg']

    data = {
        'col1': ['Lorem ipsum', 'dolor sit', 'amet, consectetur', 'adipiscing elit'],
        'col2': ['Sed do', 'eiusmod tempor', 'incididunt ut', 'labore et dolore'],
        'col3': ['Ut enim', 'ad minim veniam', 'quis nostrud exercitation', 'ullamco laboris']
    }

    df = pd.DataFrame(data)

    col3 = multi_apply(df, 'col3', ['vowels_removed', 'words_reversed', 'dupes_removed'], [StringOperations.remove_vowels, StringOperations.word_reversal, StringOperations.remove_duplicates])
    result_col3 = [['Lorem ipsum', 'Sed do', 'Ut enim', 't nm', 'enim Ut', 'Ut enim'], ['dolor sit', 'eiusmod tempor', 'ad minim veniam', 'd mnm vnm', 'veniam minim ad', 'ad minve'], ['amet, consectetur', 'incididunt ut', 'quis nostrud exercitation', 'qs nstrd xrcttn', 'exercitation nostrud quis', 'quis notrdexca'], ['adipiscing elit', 'labore et dolore', 'ullamco laboris', 'llmc lbrs', 'laboris ullamco', 'ulamco bris']]
    assert col3.values.tolist() == result_col3
    assert col3.columns.tolist() == ["col1", 'col2', 'col3', 'vowels_removed', 'words_reversed', 'dupes_removed']

    col1 = multi_apply(df, 'col1', ['dupes_removed', 'words_reversed'], [StringOperations.remove_duplicates, StringOperations.word_reversal])
    result_col1 = [['Lorem ipsum', 'Sed do', 'Ut enim', 'Lorem ipsu', 'ipsum Lorem'], ['dolor sit', 'eiusmod tempor', 'ad minim veniam', 'dolr sit', 'sit dolor'], ['amet, consectetur', 'incididunt ut', 'quis nostrud exercitation', 'amet, consur', 'consectetur amet,'], ['adipiscing elit', 'labore et dolore', 'ullamco laboris', 'adipscng elt', 'elit adipiscing']]
    assert col1.values.tolist() == result_col1
    assert col1.columns.tolist() == ['col1', 'col2', 'col3', 'dupes_removed', 'words_reversed']