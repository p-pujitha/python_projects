
def top_valid_hexadecimal_words(input,count):
    result=[]
    f=open(input,'r')  #opening the file in read mode
    for l in f:
        try:
            l=l.strip()  #removing white spaces
            value=int(l,16) #hexadecimal value is stored in the variable value
            result.append((value,l))
        except ValueError as ve:
            pass
    result.sort(reverse=True) #sorting in descending order in order to get top words
    result=result[:count]
    print result



top_valid_hexadecimal_words("corncob_lowercase.txt",5)
