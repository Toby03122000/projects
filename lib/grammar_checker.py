def grammar_checker(text):
    if not text:
        raise Exception('No text given.')
    return text[0].isupper() and text[-1] in '.!?'