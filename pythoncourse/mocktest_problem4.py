__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
Return the top n most frequently occurring chars and their respective counts
e.g aaaaaabbbbcccc, 2 should return [(a 5) (b 4)]
in case of a tie, return char which comes earlier in alphabet ordering
e.g. cdbba,2 -> [(b,2) (a,1)]
use standard types and and builtin functions we have used in the course.

constraints:
1. raise TypeError if word is not a str or n is not an int
2. raise ValueError if n <= 0,
3. if n > number of unique chars just return the available chars and their counts
2. The function should be case sensitive (ie) A and a are different. So aaAABBB, 2 should return [(B,3), (A,2)]
'''

def top_chars(word, n):
    if type(word).__name__!='str' or type(n).__name__!='int':
        raise TypeError
    else:
        ans=set(word)
        ans=list(ans)
        counting=[]
        for i in range(len(ans)):
            c=word.count(ans[i])
            counting.append(c)
        final=zip(ans,counting)
        final.sort()
        i=0
        returning=[]
        while i in range(n):
            returning.append(final[i])
            i=i+1
        print returning
        return returning


    pass


#write your own tests.
def test_top_chars():
    assert [('c',2),('d',1)] == top_chars("ccd",2)
    assert [('a',5),('b',4)] == top_chars("aaaaabbbbcccdde", 2)


