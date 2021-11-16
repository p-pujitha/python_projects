__author__ = 'Kalyan'

notes = '''
Again while this code passes the tests, this code is wrong as it has been modified for the sake of the tests.

Write a test case that will fail this test. Ignore infinite sequences for now.
'''

def generator_zip(seq1, seq2, *more_seqs):
    len1=len(seq1)
    trail=type(seq2).__name__
    if trail!='generator':
        if len1>len(seq2):
            len1=len(seq2)
    if more_seqs!=():
        len2=min(len(x) for x in more_seqs)
        if len1>len2:
            len1=len2
    result1=[]
    for x in range(len1):
        result2=[]
        result2.append(seq1[x])
        if trail!='generator':
            result2.append(seq2[x])
        else:
            result2.append(seq2.next())
        if more_seqs!=():
            for y in range(len(more_seqs)):
                result2.append(more_seqs[y][x])
        yield tuple(result2)


# add some test inputs that fail with the above code, then fix the above code.
def test_generator_zip_student():
    pass

def test_generator_zip():
    gen = generator_zip(range(5), range(3), range(4), range(5))
    assert type(gen).__name__ == 'generator'
    check_generator(gen, 3, 4)

    gen = generator_zip(range(5), range(3), range(2))
    assert type(gen).__name__ == 'generator'
    check_generator(gen, 2, 3)

    gen = generator_zip(range(1, 5), "abc", [1, 2])
    assert [(1, 'a', 1), (2, 'b', 2)] == list(gen)

    gen = generator_zip((1, 2), "abcd")
    assert [(1, 'a'), (2, 'b')] == list(gen)

def check_generator(gen, max_count, tuple_length):
    for x in range(max_count):
        result = next(gen)
        assert len(result) == tuple_length, "invalid length"
        for element in result:
            assert x == element, "unexpected value"

    try:
        next(gen)
        assert False, "generator did not finish as expected"
    except StopIteration as se:
        pass


# this will run only on our runs and will be skipped on your computers.
# DO NOT EDIT
import pytest
def test_generator_zip_server():
    servertests = pytest.importorskip("unit6_server_tests")
    servertests.test_generator_zip(generator_zip)
