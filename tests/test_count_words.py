from lib.count_words import *

# A function called count_words that takes a string as an argument
# and returns the number of words in that string.


"""
Given an empty string
Return 0
"""
def test_given_empty_string_return_0():
    result = count_words('')
    assert result == 0

"""
Given a 1 word string
Return 1
"""
def test_given_1_word_string_return_1():
    result = count_words('Jeans')
    assert result == 1

"""
Given a 2 word string
Return 2
"""
def test_given_2_word_string_return_2():
    result = count_words('Pineapple express')
    assert result == 2

"""
Given a 3 word string
Return 3
"""
def test_given_3_word_string_return_3():
    result = count_words('I like pillows')
    assert result == 3

"""
Given a 3 word string with empty space
Return 3
"""
def test_given_3_word_string_with_empty_space_return_3():
    result = count_words('  I like pillows  ')
    assert result == 3