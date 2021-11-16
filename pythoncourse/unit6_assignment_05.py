__author__ = 'Kalyan'

notes = '''
1. Read instructions for the function carefully and constraints carefully.
2. Try to generate all possible combinations of tests which exhaustively test the given constraints.
3. If behavior in certain cases is unclear, you can ask on the forums
'''
from placeholders import *

# Convert a sentence which has either or to only the first choice.
# e.g we could either go to a movie or a hotel -> we could go to a movie.
# note: do not use intermediate lists (string.split), only use string functions
# assume words are separated by spaces. you can use control flow statements
# So sentence is of form <blah> either <something> or <somethingelse> and gets converted to <blah> <something>
# if it is not of the correct form, you just return the original sentence.
import re
def prune_either_or(sentence):
    list1=re.findall(r'\w+', sentence)
    len1=len(list1)
    count=0
    for i in list1:
        count+=1
        if i=="or":
            return sentence
        elif i=="either":
            list1.remove(i)
            break
    count-=1
    for i in range(count,len(list1)):
        if list1[i]=="or":
            list1=list1[0:i]
            break
    sentence=""
    for word in list1:
        sentence += " " + word
    sentence=sentence.lstrip()
    return sentence







def test_prune_either_or_student():
    assert "iam you"==prune_either_or("iam either you or he")
    assert "iam you"==prune_either_or("iam either you or either ypu or he she")
    assert "iam or"==prune_either_or("iam or")


# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_prune_either_or_server():
    servertests = pytest.importorskip("unit6_server_tests")
    servertests.test_prune_either_or(prune_either_or)
