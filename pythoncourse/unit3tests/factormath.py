
def factorize_number(number):   #Factorize the given number
    result=[]
    if number==1 or number==0:
        return result
    elif number<0:
        raise ValueError
    elif type(number).__name__ != 'int' and type(number).__name__ != 'long':
        raise TypeError

    else:
        i=2
        while i<=number:
            if(number%i==0):
                count=0
                j=1
                while j<=i/2:
                    if i%j==0:
                        count+=1
                        if count >1:
                            break
                    j+=1
                if count==1:
                    count1=0
                    while number%i==0:
                        number/=i
                        count1+=1
                    result.append((i,count1))
            i+=1
        return result

def get_hcf(first,second): # To find the hcf initially I converted first into a number and second into a number and
                            #finally do hcf

   try:
        a=function(first)
        b=function(second)
        res=0
        print a
        print b
        if a<b:
         min=a
        else:
         min=b
        print min
        for i in range(min,0,-1):
            if a%i == 0 and b%i==0:
                print i
                res=i
                break

        result=factorize_number(res)
        return result

   except OverflowError as oe:
       print oe





def function(input):  # Converting the given list into a single number

    mul=1
    a=len(input)
    for j in range(a):
        a=input[j]
        mul=mul*power(a)

    return mul


def power(input):
    a=input[0]
    b=input[1]
    result =1
    for i in range(b):
        result*=a
    return result


def get_lcm(first,second) : # LCM of 2 numbers

    a=function(first)
    b=function(second)
    res=0
    if a>b:
        max=a
    else:
        max=b

    while(True):

        if ((max%a == 0) and (max%b ==0)):
            res=max
            break
        max+=1
    result = factorize_number(res)
    return result

def multiply(first, second):   # multiply the 2 numbers
    a=function(first)
    b=function(second)
    res=a*b
    result = factorize_number(res)
    return result