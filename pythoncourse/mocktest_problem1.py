__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
Given a sentence in which words are separated by spaces.

Re-arrange it so that words are reordered according to the following criteria.
 - longer words come before shorter words
 - if two words have same length, the one with smaller vowel occurance count comes first (feeel counts as 3 vowel occurances)
 - if even that is same, preserve the original order.

Constraints:
- Only allowed characters are a-zA-Z in the words
- raise a ValueError if the sentence contains any characters beyond the above
- raise a TypeError if input is not a string
- The result should preserve the words as is without changing case etc. but the sentence should be sorted so that
longer words precede shorter words. In case of tie, the word with fewer vowels comes first, if there is a tie even there,
preserve the original order.
- If there are multiple spaces, merge them into a single space in the result.
- If there is any leading or trailing space, remove it from the result.

Note: use the features of python to solve this problem, DON'T WRITE YOUR OWN SORT ROUTINE!
'''

def transform(sentence):
    if type(sentence).__name__!='str':
        raise TypeError
    else:


        try:
            listing =[]
            letters=[]
            for i in range(len(sentence)):
                if(sentence[i]==' '):
                    word="".join(letters)
                    listing.append(word)
                    letters=[]
                else:
                    letters.append(sentence[i])
            word="".join(letters)
            listing.append(word)
            var=listing
            var.sort(key=lambda x:len(x), reverse=True)
            print var
            vowels=set("aeiou")
            resultfinal=[]
            countlessvowels=[]
            wordsinvowels=[]
            i=0
            while i in range(len(var)+1):
                if len(var[i])== len(var[i+1]):
                    wordsinvowels.append(var[i])
                    wordsinvowels.append(var[i+1])
                    count=0
                    for j in range(len(var[i])):
                        if var[i][j] in vowels:
                            count=count+1
                    countlessvowels.append(count)

                    count=0
                    for j in range(len(var[i+1])):
                        if var[i+1][j] in vowels:
                            count=count+1
                    countlessvowels.append(count)
                    resultfinal.append(wordsinvowels[countlessvowels.index(min(countlessvowels))])
                    del wordsinvowels[countlessvowels.index(min(countlessvowels))]
                    resultfinal.append(wordsinvowels[countlessvowels.index(max(countlessvowels))])
                    countlessvowels=[]
                    wordsinvowels=[]
                    i=i+2
                else:
                    resultfinal.append(var[i])
                    i=i+1

            print resultfinal
        except IndexError as ae:
            print ae
        resultfinal.append(var[i])




        result=[]
        for i in range(len(resultfinal)):
                for j in range(len(resultfinal[i])):
                    result.append(resultfinal[i][j])
                if i !=len(resultfinal)-1:
                    result.append(' ')
        print result
        print "".join(result)
        return "".join(result)







    pass


def test_transform():
    assert "elephant walking runway down seen was the An" == transform("An elephant was seen walking down the runway")