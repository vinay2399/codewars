def get_count(input_str):
    num_vowels = 0
    # your code here
    for i in input_str:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            num_vowels+=1
    return num_vowels
