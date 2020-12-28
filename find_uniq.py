def find_uniq(arr):
    d={}
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return [val for val in d.keys() if d[val]==1][0]
