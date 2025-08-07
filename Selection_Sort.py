'''Selection Sort Algorithm                                    28-07-2025
   sorting algorithms that works by repeatedly finding the minimum element
   from the unsorted part of the array and putting it at the beginning of 
   the unsorted region of the array.

'''
# arr=[18,10,8,20,21,3]
arr=[29,72,98,13,27,87,66,52,51]
def selection_sort(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
          if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
    return arr        
print(selection_sort(arr))
