__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
 This problem deals with number conversion from a custom base 26 notation.

 In this notation, the letters a to z are used for digits 0 to 25. E.g.
 decimal 10 in this notation will be "k" and 26 will be "ba" The notation in
 case insensitive so even Ba is a valid representation for 26.

 Your job is to write a decoding routine for this notation.

 Note: make good use of python features and avoid huge if else statement flow!
'''

import string

# Notes:
# - if s is not a string, raise TypeError
# - if the encoding is not right or empty string, raise ValueError
# - allow both - and + as prefixes which represent sign.
# - allow trailing and starting spaces (but not once the sign or number starts)
# - allow both capital and small letters.
# - return a int or long that corresponds to the number.
def from_custom_base26(s):
    if type(s).__name__!="str":
        raise TypeError
    value=0
    for x in s:
        if ord(x.upper())<65 or ord(x.upper())>90:
            raise ValueError
    type1=0
    for x in s:
        assci=ord(x.upper())
        value+=assci-65
        value+=type1
        type1=25
    return value


# a basic test is given, write your own tests based on constraints.
def test_from_custom_base26():
    assert 29 == from_custom_base26("bd")