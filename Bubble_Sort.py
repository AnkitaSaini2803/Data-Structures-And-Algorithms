# Bubble Sort Algorithm                                      #2-08-2025

arr=[5,1,8,6,9,2,4]
def bubble_sort(arr):
    for i in range(0,len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
print(bubble_sort(arr))

# bubble_sort(arr)
# print(arr)
'''You do not need to return anything because changes are made directly
to the original array/list '''

def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    