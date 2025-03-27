
def linear_search(arr,n):
    for i in range(len(arr)):
        if arr[i]==n:
            return i
    
    return -1
            
arra=list(map(int,input("Enter the array element : ").split()))
target=int(input("Enter the target value : "))
result=linear_search(arra,target)
print("Element found at index:",result) if result!=-1 else print("Element not found")


 