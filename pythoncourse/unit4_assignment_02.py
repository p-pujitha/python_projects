__author__ = 'Kalyan'

notes='''
 This is a basic problem involving some file reading and writing. You can put what you have learnt in earlier units
 to use here - functions or nested functions, lists, sorting, generators(optional), comprehensions (optional) etc.

1. Review the relevant lessons if you are blocked.
2. Do not modify the given input files :), modify your code to handle them.
3. Write helper routines where as needed.
3. You can write your own test routines like test_sort_words2(), but comment them out before submitting.
'''

import unit4utils

def sort_words(source, destination):
    """
    Sort the words in the file specified by source and put them in the
    file specified by destination. The output file should have only lower
    case words, so any upper case words from source must be lowered.

    Ignore empty lines or lines starting with #
    """
    f1= open(source,"r")
    lines=[]
    for f in f1:
        if f[0]!='#' and f[0]!=' ' and f[0]!='\n':
            if f[-1]!='\n':
                f=f+'\n'
            lines.append(f.lower())
    lines.sort()
    lines = ' '.join(lines)
    f1=open(destination,"w")
    f1.write(lines)
    f1.close()






def test_sort_words():
    source = unit4utils.get_input_file("unit4_testinput_02.txt")
    expected = unit4utils.get_input_file("unit4_expectedoutput_02.txt")
    destination = unit4utils.get_temp_file("unit4_output_02.txt")
    sort_words(source, destination)
    result = [word.strip() for word in open(destination)]
    expected = [word.strip() for word in open(expected)]
    assert expected == result
