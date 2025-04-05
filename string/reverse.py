def reverse_a_string(s):
    reverse=''
    for i in s:
        reverse=i+reverse
    return reverse
    
    
result=reverse_a_string(input("Enter a string : "))
print(result)