## 1. Describe the Problem

'''
As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.
'''

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

'''
def time_manager(text):
    Parameters: text: a string containing a series of words e.g. 'The quick brown fox jumps over the lazy dog'
    Return value: estimated reading time in minutes: an fstring joining a float and a string e.g. '5.0 minutes'
'''

```python

def time_manager(text):
    '''Provides estimated reading time based on length of text
    
    Parameters:
        text: a string containing a series of words e.g. 'The quick brown fox jumps over the lazy dog'

    Returns:
        estimated reading time: an fstring joining a float and a string e.g. '5.0 minutes'
    '''

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

"""
Given an empty string
It returns the message: '0.0 minutes'
"""
time_manager('') => '0.0 minutes'

"""
Given a string of 200 words
It returns the message: '1.0 minutes'
"""
time_manager('') => '1.0 minutes'

"""
Given a string of 400 words
It returns the message: '2.0 minutes'
"""
time_manager('') => '2.0 minutes'

"""
Given a string of 300 words
It returns the message: '1.5 minutes'
"""
time_manager('') => '1.5 minutes'
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python

```

Ensure all test function names are unique, otherwise pytest will ignore them!