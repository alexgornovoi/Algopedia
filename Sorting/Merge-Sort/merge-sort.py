def merge_sort(arr):
    if len(arr) <=1:
        return arr
    
    mid = len(arr) // 2
    arr1 = merge_sort(arr[:mid])
    arr2 = merge_sort(arr[mid:])
    
    return merge(arr1,arr2)
    
def merge(arr1, arr2):
    pos1 = pos2 = 0
    arr = []
    
    while pos1 < len(arr1) and pos2 < len(arr2):
        if arr1[pos1] < arr2[pos2]:
            arr.append(arr1[pos1])
            pos1 += 1
        else:
            arr.append(arr2[pos2])
            pos2 += 1
        
    arr += arr1[pos1:]
    arr += arr2[pos2:]
    
    return arr