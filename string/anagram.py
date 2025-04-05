def check_anagram(first,second):
    character_count1={}
    character_count2={}
    
    if len(first)!=len(second):
        return False
    else:
        for char in first:
            if char in character_count1:
                character_count1[char]+=1
            else:
                character_count1[char]=1
        for char in second:
            if char in character_count2:
                character_count2[char]+=1
            else:
                character_count2[char]=1
            
    return character_count2==character_count1

        

string1=input("enter the first  :")
string2=input("enter the second :")
result=check_anagram(string1,string2)
print(result)