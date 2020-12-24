def anagrams(word, words):
    #your code here
    l=[]
    for i in words:
        if len(word)==len(i):
            if set(word)==set(i):
                l.append(i)
    return l
