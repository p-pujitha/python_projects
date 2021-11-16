__author__ = 'Kalyan'

notes = '''
Implement a left binary search and write exhaustive tests for the same. Left binary search returns the left most
element when a search key repeats. For e.g if input is [1,2,3,3,4,4,5] and I search 3, it should return 2 as index 2 is
the left most occurance of 3.

In [1,1,1,1,1,1,1,1], I search for 1, you should return 0.

Note that we are looking for a binary search => we want not more than log(N) lookups, so a solution that involves finding
a random 1 and then doing a linear scan to the left is not a solution :).
'''
def left_binary_search(input, value):
    input_len=len(input)
    start=0
    end=input_len-1
    if len>0:
        mid=(start+end)/2
        while mid>=0 and mid<input_len and start<=end:
            if (input[mid]==value and input[mid-1]!=value )or (mid-1<0 and input[mid]==value):
                return mid
            elif input[mid]>=value:
                end=mid-1
            elif input[mid]<value:
                start=mid+1


            mid=(start+end)/2
    return -1


# write your own exhaustive tests :)
def test_left_binary_search_student():
    assert 0==left_binary_search([1,1,1,1,1,1,1,1],1)
    assert -1==left_binary_search([1,1,1,1,1,1,1,1],2)
    assert  9 ==left_binary_search([1,1,1,1,1,1,1,1,1,2],2)


# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_left_binary_search_server():
    servertests = pytest.importorskip("unit6_server_tests")
    servertests.test_left_binary_search(left_binary_search)
