def get_middle(s):
    l=len(s)
    if(l%2==0):
        l2=int(l/2)
        return s[l2-1]+s[l2]
    else:
        l2=int((l+1)/2)
        return s[l2-1]
        #your code here
