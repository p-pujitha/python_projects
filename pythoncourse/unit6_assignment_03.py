__author__ = 'Kalyan'

notes = '''
Now we move on to writing both the function and the tests yourself.

In this assignment you have to write both the tests and the code. We will verify your code against our own tests
after you submit.
'''

# fill up this routine to test if the 2 given words given are anagrams of each other. http://en.wikipedia.org/wiki/Anagram
# your code should handle
#  - None inputs
#  - Case  (e.g Tip and Pit are anagrams)
def are_anagrams(first, second):
    if (len(first)!=len(second)):
        return False

    else:
        first=first.lower()
        second=second.lower()
        a=list(first)
        b=list(second)
        if a.sort()!=b.sort():
            return False
        else:
            return True



# write your own exhaustive tests based on the spec given
def test_are_anagrams_student():
    assert True == are_anagrams("pit", "tip") #sample test.

def test_are_anagrams_student():
    assert True == are_anagrams("Act", "tac") #sample test.

def test_are_anagrams_student():
    assert True == are_anagrams("PIT", "pit") #sample test.

def test_are_anagrams_student():
    assert False == are_anagrams("AACCTT", "tac") #sample test.

# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_are_anagrams_server():
    servertests = pytest.importorskip("unit6_server_tests")
    servertests.test_are_anagrams(are_anagrams)
