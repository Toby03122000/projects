from lib.grammar_checker import *
import pytest

"""
Given a string with no leading capital letter
It returns: False
"""
def test_no_cap():
    result = grammar_checker('the quick brown fox jumps over the lazy dog')
    assert result == False

"""
Given a string with no suitable ending punctuation
It returns: False
"""
def test_no_punc():
    result = grammar_checker('the quick brown fox jumps over the lazy dog')
    assert result == False

"""
Given a string with a leading capital letter
It returns: True
"""
def test_with_cap():
    result = grammar_checker('The quick brown fox jumps over the lazy dog.')
    assert result == True

"""
Given a string with suitable ending punctuation
It returns: True
"""
def test_with_punc():
    result = grammar_checker('The quick brown fox jumps over the lazy dog.')
    assert result == True

"""
Given a string with no leading capital letter or suitable ending punctuation
It returns: False
"""
def test_no_cap_no_punc():
    result = grammar_checker('the quick brown fox jumps over the lazy dog')
    assert result == False

"""
Given a string with a leading capital letter but no suitable ending punctuation
It returns: False
"""
def test_with_cap_no_punc():
    result = grammar_checker('The quick brown fox jumps over the lazy dog')
    assert result == False

"""
Given a string with no leading capital letter but suitable ending punctuation
It returns: False
"""
def test_with_punc_no_cap():
    result = grammar_checker('the quick brown fox jumps over the lazy dog.')
    assert result == False

"""
Given an empty string
It returns: error
"""
def test_empty_string():
    with pytest.raises(Exception) as e:
        result = grammar_checker('')
    error_message = str(e.value)
    assert error_message == 'No text given.'