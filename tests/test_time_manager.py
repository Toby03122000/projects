from lib.time_manager import *

"""
Given an empty string
It returns the message: '0.0 minutes'
"""
def test_given_empty_string_return_0_mins():
    result = time_manager('')
    assert result == '0.0 minutes'

"""
Given a string of 200 words
It returns the message: '1.0 minutes'
"""
def test_string_of_200_words_return_1_mins():
    text = ' '.join(['word' for i in range(0, 200)])
    result = time_manager(text)
    assert result == '1.0 minutes'

"""
Given a string of400 words
It returns the message: '2.0 minutes'
"""
def test_string_of_400_words_return_2_mins():
    text = ' '.join(['word' for i in range(0, 400)])
    result = time_manager(text)
    assert result == '2.0 minutes'

"""
Given a string of 300 words
It returns the message: '1.5 minutes'
"""
def test_string_of_300_words_return_1_point_5_mins():
    text = ' '.join(['word' for i in range(0, 300)])
    result = time_manager(text)
    assert result == '1.5 minutes'

"""
Given a string of 100 words
It returns the message: '0.5 minutes'
"""
def test_string_of_100_words_return_0_point_5_mins():
    text = ' '.join(['word' for i in range(0, 100)])
    result = time_manager(text)
    assert result == '0.5 minutes'