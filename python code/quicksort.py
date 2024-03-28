def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)
        
    
arr = [1, 2, 9, 3, -2, 4, 6]
sorted_arr = quicksort(arr)
print('Sorted array in ascending order: ')
print(sorted_arr)