digits = '1234567890'

def count_digits(line=''):
    digits_number = 0
    for symbol in line:
        if symbol in digits:
            digits_number += 1
    return digits_number

