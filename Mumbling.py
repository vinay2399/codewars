def accum(s):
    flag=0
    m=''
    if s.isalpha():
        for i in range(0,len(s)):
            if flag==0:
                m+=s[i].upper()
                flag=1
            if flag==1:
                for j in range(1,i+1):
                    m+=s[i].lower()
                flag=0
                m+='-'
        return m[:-1]
