def binary_array_to_number(arr):
  # your code
    decimal=0
    s=''
    for i in arr:
        if i!='':
            s+=str(i)
    for i in s:        
        decimal = decimal*2 + int(i)
    return decimal
