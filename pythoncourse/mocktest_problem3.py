__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
Pig latin is an amusing game to conceal the meaning of a sentence.

Rules for converting a word to pig latin are as follows:

1. If word starts with a consonant, move all continuous consonants before the first vowel to the end and add  "ay" at the end.
e.g  happy becomes appyhay, trash becomes ashtray, dog becomes ogday etc.

2. If word starts with a vowel, you just add an ay. e.g. egg become eggay, eight becomes eightay etc.

Your job is to write a routine that will convert a given text to pig latin. e.g "There is, however, no need for fear."
should get converted to  "Erethay isay, oweverhay, onay eednay orfay earfay."  Note that punctuation and
capitalization has to be preserved

You can write helper sub routines to make your code easy to read and write.

Constraints: only punctuation allowed is , and . and they will come immediately after a word and
will be followed by a space if there is a next word. Acronyms are not allowed in sentences.
Some words may be capitalized (first letter is capital like "There" in the above example)
and you have to preserve its capitalization in the final word too (Erethay)

You can assume that only valid inputs as specified above will be given.
'''

def get_pig_latin(sentence):
    vowels=set("aeiou")
    ans=[]
    ans2=[]
    i=0
    f=0
    flag=0
    final_result=[]
    while i in range(len(sentence)):
        if(sentence[i] not in vowels and f==0):
            f=1
            ans.append(sentence[i])
        if sentence[i] in vowels:

            ans2.append(sentence[i])



        if(sentence[i]==' ' or i==len(sentence)-1):
            for i in range(len(ans2)):
                final_result.append(ans2[i])
            for i in range(len(ans)):
                final_result.append(ans[i])
            appending="ay"
            for i in range(len(appending)):
                final_result.append(appending[i])
            if i!=len(sentence)-1:
                final_result.append(' ')
        i=i+1

    print final_result
    return "".join(final_result)





    pass


# write your own tests according to the constraints and notes given above.
def test_get_pig_latin():
        assert "onay earfay" == get_pig_latin("no fear")



