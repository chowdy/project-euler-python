"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are
3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be
used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and
115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance
with British usage.
"""
ONES = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

TEENS = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
}

TENS = {
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'
}

HUNDRED = 'hundred'
THOUSAND = 'thousand'


def solution():
    words = ''
    for i in range(1, 1000+1):
        print(f'> {i}')
        word = ''
        if i == 1000:
            word += 'onethousand'
        else:
            if i >= 100:
                hundreds = int(i / 100)
                word += ONES[hundreds] + HUNDRED
                i -= hundreds * 100
                if i != 0:
                    word += 'and'
            if 10 <= i < 20:
                word += TEENS[i]
            elif i >= 20:
                tens = int(i / 10) * 10
                word += TENS[tens]
                i -= tens
            if 0 < i < 10:
                word += ONES[i]
        print(f'= {word}')
        words += word
    return len(words)
