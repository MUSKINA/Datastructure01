def string_compression(word):
    if not word:  # Handle empty input
        return ""
    c_string=""
    count=1
    for i in range(len(word)-1):
        if word[i]==word[i+1]:
            count+=1
        else:
            c_string+=word[i]+str(count)
            count=1
            
    c_string+=word[-1]+str(count)
    return c_string if len(c_string) < len(word) else word

    
result=string_compression(input("Enter the string : "))
print(result)