def sort_array(source_array):
    # Return a sorted array.
    oi=[]
    sorted=[]
    for i in source_array:
        if i%2!=0:
            oi.append(i)
            sorted.append("a")
        else:
            sorted.append(i)
    oi.sort()
    for i in oi:
        a=sorted.index("a")
        sorted[a]=i
        
    return sorted

        
