
def startingfunction():
    words_in_file=open("corncob_lowercase.txt", 'r')
    words=[word.strip() for word in words_in_file]
    top_n_splitting_words=splitting_output(words,5)
    for i in range(5):
        print top_n_splitting_words[i][0] ,"->" ,top_n_splitting_words[i][1]


def splitting_output(words, n):
    words=set(words)
    result=[]
    answer=[]
    for word in words:
        length=len(word)
        for i in range(length):
            if(word[:i] in words and word[i:] in words):
                answer.append((word[:i], word[i:]))
        result.append([word, answer])
        answer=[]


    result.sort(key=lambda x:x[0],reverse=True)
    result.sort(key=lambda x:len(x[1]), reverse=True)

    returning_answer=result[:n]
    #for i in range(n):
        #returning_answer.append(result[i])
    return returning_answer

startingfunction()