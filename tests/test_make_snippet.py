from lib.make_snippet import *

# A function called make_snippet that takes a string as an argument
# and returns the first five words and then a '...' if there are more than that.

"""
Given empty string
Return empty string
"""
def test_given_empty_string_return_empty_string():
    result = make_snippet('')
    assert result == ''

"""
Given string less than 6 words
Return same string
"""
def test_given_string_less_than_6_words_return_same_string():
    result = make_snippet('King Harold the Great')
    assert result == 'King Harold the Great'

"""
Given string longer than 5 words
Return first 5 words only + '...'
"""
def test_given_string_longer_than_5_words_return_first_5_words_only_and_ellipsis():
    result = make_snippet('King Harold sat magnificently upon his mushroom toadstool')
    assert result == 'King Harold sat magnificently upon...'