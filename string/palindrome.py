def palindrome(s):
    rev_s=s[::-1]
    if s==rev_S:
        return f"{s} is a palindrome"
    else:
        return f"{s} not a palindrome"     
    
    
    
result=palindrome(input("Enter the string : "))
print(result)


def palindrome(s):
    rev_s=''
    for i in range(len(s)-1,-1,-1):
        rev_s=rev_s+s[i]
    if s==rev_s:
        return f"{s} is a palindrome"
    else:
        return f"{s} not a palindrome"     
    
    
    
result=palindrome(input("Enter the string : "))
print(result)