__author__ = 'Kalyan'

notes = '''
Write your own implementation of converting a number to a given base.
It is important to have a good logical
and code understanding of this.

Till now, we were glossing over error checking, for this function do proper error checking and raise exceptions
as appropriate.

Reading material:
    http://courses.cs.vt.edu/~cs1104/number_conversion/convexp.html
'''
def reversing(name):
    rev_name=''
    for i in range(len(name)-1,-1,-1):
       rev_name+=name[i]
    return rev_name


def convert(number, base):
    """
    Convert the given number into a string in the given base. valid base is 2 <= base <= 36
    raise exceptions similar to how int("XX", YY) does (play in the console to find what errors it raises).
    Handle negative numbers just like bin and oct do.
    """
    if type(number).__name__ != 'int' or type(base).__name__ != 'int' :
        raise TypeError
    elif base < 2 or base > 36:
        raise ValueError
    else:
        flag=0
        result=""
        if number<0:
            flag=1
        number=abs(number)
        if number>=0:
            while base<=number:
                div=number%base
                number=number/base
                if div<10:
                    result=result+str(div)
                else:
                    result=result+chr(55+div)

            if number<10:
                result=result+str(number)
            else:
                result=result+chr(55+number)


        if flag==0:
            return reversing(result)
        else:
            return '-'+reversing(result)


    #pass


def test_convert():
    assert "100" == convert(4,2)
    assert "FF" == convert(255,16)
    assert "377" == convert(255, 8)
    assert "JJ" == convert(399, 20)
    assert "-JJ" == convert(-399, 20)

    try:
        convert(10,1)
        assert False, "Invalid base <2 did not raise error"
    except ValueError as ve:
        print ve

    try:
        convert(10, 40)
        assert False, "Invalid base >36 did not raise error"
    except ValueError as ve:
        print ve

    try:
        convert("100", 10)
        assert False, "Invalid number did not raise error"
    except TypeError as te:
        print te

    try:
        convert(None, 10)
        assert False, "Invalid number did not raise error"
    except TypeError as te:
        print te


    try:
        convert(100, "10")
        assert False, "Invalid base did not raise error"
    except TypeError as te:
        print te