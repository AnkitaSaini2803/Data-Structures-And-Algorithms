#BINARY SEARCH USING RECURSIVE APPROACH

nums=[2,5,7,9,10,23,34,50]
target=3
n=len(nums)
st,end=0,n-1
def binarysearch(nums,st,end):
    if st>end:
        return -1
    mid=(st+end)//2
    if target==nums[mid]:
        return mid
    elif target<nums[mid]:
        return binarysearch(nums,st,mid-1)
    elif target>nums[mid]:
        return binarysearch(nums,mid+1,end)
    else:
        return -1
print(binarysearch(nums,st,end))
