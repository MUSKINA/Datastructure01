def longest_common_prefix(s):
    if not s:
        return "No common prefix"
    s.sort()
    print(s)
    common_prefix=''
    first,last=s[0],s[-1]
    for i in range(0,min(len(first),len(last))):
        if first[i]==last[i]:
            common_prefix+=first[i]
        else:
            break
    return common_prefix if common_prefix else "No common prefix"
            
    
result=longest_common_prefix(list(input("Enter the strings : ").split()))
print(f"Longest common prefix  : {result}")