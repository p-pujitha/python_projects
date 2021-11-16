__author__ = 'Kalyan'

notes = '''
Though it might appear as if the given tests should be able to catch all logical bugs in de_dup_and_sort, that is not the
case as the code below shows.

So be clear that some blackbox tests alone are no substitute for reasoning/taking care of the correctness yourself.

Now add a test that fails with the given code.
'''
def de_dup_and_sort(input):
    """
    Given an input list of strings, return a list in which the duplicates are removed and the items are sorted.
    """

    input = set(input)

    input = list(input)
    input.sort()
    return input


# add an test input that fails with above code and then fix the above code.
def test_de_dup_and_sort_student():
    assert ["1","2","3"] == de_dup_and_sort(["3", "3", "2", "2","1","1"])
    assert [ 'i', 'j', 'p','u'] == de_dup_and_sort(list("puji"))
    assert ['1', '2', '3'] == de_dup_and_sort(list("332211"))

def test_de_dup_and_sort():
    assert ["a", "b"] == de_dup_and_sort(["b", "a", "b", "a"])
    assert ["a"] == de_dup_and_sort(["a", "a", "a"])
    assert [] == de_dup_and_sort([])
    assert ["a", "b"] == de_dup_and_sort(["a", "b"])
    assert ["a", "b"] == de_dup_and_sort(["a", "b"]*10)


# this will run only on our runs and will be skipped on your computers.
# DO NOT EDIT
import pytest
def test_de_dup_and_sort_server():
    servertests  = pytest.importorskip("unit6_server_tests")
    servertests.test_de_dup_and_sort(de_dup_and_sort)
