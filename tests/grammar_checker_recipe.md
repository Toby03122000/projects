## 1. Describe the Problem

'''
As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.
'''

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

'''
def grammar_checker(text):
    Parameters:
        text: a string containing a series of words e.g. 'The quick brown fox jumps over the lazy dog.'
    Return value:
        True: a boolean if the text starts with a capital letter AND ends with one of the following: '.!?'
        False: a boolean if the above is not so
'''

```python

def grammar_checker(text):
    '''Verifies that a text starts with a capital letter AND ends with one of the following: '.!?'
    
    Parameters:
        text: a string containing a series of words e.g. 'The quick brown fox jumps over the lazy dog.'

    Returns:
        True: a boolean if the text starts with a capital letter AND ends with one of the following: '.!?'
        False: a boolean if the above is not so
    '''

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

"""
Given a string with no leading capital letter
It returns: False
"""
grammar_checker('the quick brown fox jumps over the lazy dog') => False

"""
Given a string with no ending punctuation
It returns: False
"""
grammar_checker('the quick brown fox jumps over the lazy dog') => False

"""
Given a string with a leading capital letter
It returns: True
"""
grammar_checker('The quick brown fox jumps over the lazy dog') => True

"""
Given a string with an ending '.'
It returns: True
"""
grammar_checker('The quick brown fox jumps over the lazy dog.') => True

"""
Given a string with an ending '.'
It returns: True
"""
grammar_checker('The quick brown fox jumps over the lazy dog.') => True

"""
Given a string with an ending '!'
It returns: True
"""
grammar_checker('The quick brown fox jumps over the lazy dog!') => True

"""
Given a string with an ending '?'
It returns: True
"""
grammar_checker('The quick brown fox jumps over the lazy dog?') => True

"""
Given a string with a leading capital letter AND suitable ending punctuation
It returns: True
"""
grammar_checker('The quick brown fox jumps over the lazy dog.') => True

"""
Given an empty string
It returns: error_message = 'No text given.'
"""
grammar_checker('') => error_message = 'No text given.'
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python

```

Ensure all test function names are unique, otherwise pytest will ignore them!