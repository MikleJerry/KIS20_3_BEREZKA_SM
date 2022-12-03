digits = '1234567890'

def count_digits(line=''):
    digits_number = 0
    for symbol in line:
        if symbol in digits:
            digits_number += 1
    return digits_number


def test_count_digits():
    assert count_digits() == 0
    assert count_digits('Без цифр!') == 0
    assert count_digits('Привет, 0_0 мирР!?') == 2


if __name__ == '__main__':
    print(count_digits('Цифорки: 1235'))