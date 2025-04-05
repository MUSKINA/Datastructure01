def binary_search(arr,left,right,target):
    if left>right:
        return -1
    
    mid=(left+right)//2
    if arr[mid]==target:
        return mid

    elif arr[mid]<target:
        
        return binary_search(arr,mid+1,right,target)
    else:
        
        return binary_search(arr,left,mid-1,target)
        
        


arra=list(map(int,input("Enter array elements :").split()))
arra.sort()
target=int(input("Enter the target value : "))
result=binary_search(arra,0,len(arra)-1,target)
print("Element found at index:", result) if result != -1 else print("Element not found")