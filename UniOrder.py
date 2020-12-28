def unique_in_order(iterable):
    a=[]
    c=0
    if iterable=='':
        return a
    else:
        a.append(iterable[0])
        for i in range(len(iterable)):
            if iterable[i]==a[c]:
                pass
            else:
                a.append(iterable[i])
                c+=1
        return a
