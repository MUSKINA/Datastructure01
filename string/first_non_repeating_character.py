def first_non_repeating_character(s):
    character_count={}
    for char in s:
        if char in character_count:
            character_count[char]+=1
        else:
            character_count[char]=1
    for index,char in  enumerate(s):
        if character_count[char]==1:
            return index
    return -1
            
        
    
    
result=first_non_repeating_character(input("Enter the character : "))
print(result)