from solution import *
import math

def test_all():
    lorem_ipsum = ["Lorem", "ipsum", "dolor sit",
                   "amet", "consectetur", "adipiscing"]
    fruits = ["apple", "banana", "orange", "grapefruit", "kiwi", "pear"]
    makeup = ["ultra shiny liquid lipstick", "brush", "blush",  "brown brow pomade",
              "lipgloss", "powder puff", "sponge", "brow gel", "eyeshadow palette"]
    random = ["hello", "wyatt", "amore", "zzzzz",
              "world", "banana", "brick", "hi", "rock", "a"]
    numbers_1 = [23, 56, -12, 45, 78, -9, 34, 0, 67, -5]
    numbers_2 = [50, -30, 15, 40, -20, 25, 0, 35, -10, 45]

    assert sorted(lorem_ipsum, key=Comparators.by_length) == [
        'amet', 'Lorem', 'ipsum', 'dolor sit', 'adipiscing', 'consectetur']
    assert sorted(fruits, key=Comparators.by_length) == [
        'kiwi', 'pear', 'apple', 'banana', 'orange', 'grapefruit']

    assert sorted(lorem_ipsum, key=Comparators.by_num_vowels) == [
        'Lorem', 'ipsum', 'amet', 'dolor sit', 'consectetur', 'adipiscing']
    assert sorted(fruits, key=Comparators.by_num_vowels) == [
        'apple', 'kiwi', 'pear', 'banana', 'orange', 'grapefruit']

    assert sorted(numbers_1, key=Comparators.by_numerical_value) == [
        -12, -9, -5, 0, 23, 34, 45, 56, 67, 78]
    assert sorted(numbers_2, key=Comparators.by_numerical_value) == [
        -30, -20, -10, 0, 15, 25, 35, 40, 45, 50]

    assert sorted(makeup, key=Comparators.by_word_count) == [
        'brush', 'blush', 'lipgloss', 'sponge', 'powder puff', 'brow gel', 'eyeshadow palette', 'brown brow pomade', 'ultra shiny liquid lipstick']
    assert sorted(lorem_ipsum, key=Comparators.by_word_count) == [
        'Lorem', 'ipsum', 'amet', 'consectetur', 'adipiscing', 'dolor sit']

    assert Comparators.sort_with_tiebreaker(makeup, Comparators.by_word_count, Comparators.by_num_vowels) == [
        'brush', 'blush', 'lipgloss', 'sponge', 'brow gel', 'powder puff', 'eyeshadow palette', 'brown brow pomade', 'ultra shiny liquid lipstick']
    assert Comparators.sort_with_tiebreaker(random, Comparators.by_length, Comparators.by_num_vowels) == [
        'a', 'hi', 'rock', 'zzzzz', 'wyatt', 'world', 'brick', 'hello', 'amore', 'banana']
    assert Comparators.sort_with_tiebreaker(
        [], Comparators.by_length, Comparators.by_num_vowels) == []
    assert Comparators.sort_with_tiebreaker(
        ["a"], Comparators.by_length, Comparators.by_num_vowels) == ["a"]
    assert Comparators.sort_with_tiebreaker(
        ["b", "a"], Comparators.by_length, Comparators.by_num_vowels) == ["b", "a"]
    assert Comparators.sort_with_tiebreaker(
        ["b", "a", "aaa"], Comparators.by_length, Comparators.by_num_vowels) == ["b", "a", "aaa"]
    assert Comparators.sort_with_tiebreaker(
        ["a", "b", "aaa"], Comparators.by_length, Comparators.by_num_vowels) == ["b", "a", "aaa"]
    assert Comparators.sort_with_tiebreaker(
        ["aaa", "a", "b"], Comparators.by_length, Comparators.by_num_vowels) == ["b", "a", "aaa"]