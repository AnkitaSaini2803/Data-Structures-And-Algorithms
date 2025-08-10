'''Insertion Sort Algorithm                          8-8-2025/ 10-8-2025 '''

nums=[3,5,6,4,8,9,10,7,1]
def insertion_sort(nums):
    for i in range(1,len(nums)):
        j=i-1
        key=nums[i]
        while j>=0 and nums[j]>key:
            nums[j+1]=nums[j]
            j=j-1
        nums[j+1]=key
    return nums
print(insertion_sort(nums))


