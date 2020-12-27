def reverse_words(text):

    s=''
    r=''
    for i in range(0,len(text)):
        if text[i]!=' ':
            s+=text[i]
        else:
            r+=s[::-1]
            s=''
            r+=text[i]
    r+=s[::-1]
    print(i)
    return r
