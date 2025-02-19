def capitalize(text):
    if text == '':
        return ''
    first_char = text[0].upper()
    rest = text[1:]
    return f'{first_char}{rest}'
