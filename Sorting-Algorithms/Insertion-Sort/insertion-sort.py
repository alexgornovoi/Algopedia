def insertion_sort(arr):
    pos = 0
    
    while pos < len(arr):
        curr = pos
        
        while curr > 0 and arr[curr-1] > arr[curr]:
            arr[curr], arr[curr-1] = arr[curr-1], arr[curr]
            curr -= 1
        
        pos += 1
    
    return arr