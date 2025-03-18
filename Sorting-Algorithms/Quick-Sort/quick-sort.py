def quick_sort(arr, left = 0, right = None):
    if  right is None:
        right = len(arr) - 1
        
    if left < right:
        index = partition(arr, left, right)
        quick_sort(arr, left, index - 1)
        quick_sort(arr, index, right)
    
    return arr
        

def partition(arr, left, right):
    pivot = arr[(left+right)//2]
    
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -=1

    return left