def longest(s1, s2):
    # your code
    a=s1+s2
    b=list(set(a))
    b.sort()
    st=''
    for i in b:
        st+=i
    return st
