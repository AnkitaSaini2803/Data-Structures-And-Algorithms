# WAP TO IMPLEMENT BINARY SEARCH USING ITERATIVE APPROACH      25-07-2025

nums=[5,6,9,12,15,34] 
target=12
n=len(nums)
def binary_search(nums,target):
    start=0 #start is a pointer pointing to the first index of array and
    end=n-1 #end is a ponter pointing to the end of array

    # start,end=0,n-1
    
    while start<=end:
        mid=(start+end)//2            #calculate mid of array/list
        if target==nums[mid]:
            return mid
        elif target>nums[mid]:
            start=mid+1
        elif target<nums[mid]:
            end=mid-1
    return -1
print(binary_search(nums,target))
    