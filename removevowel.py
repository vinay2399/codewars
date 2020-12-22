def disemvowel(string):
    for i in string:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
            string=string.replace(i,'')
    return string
s="This website is for losers LOL!"
print(disemvowel(s))
