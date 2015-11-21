def FirstBinarySearch(alist, k):
    low = 0
    high  = len(alist) -1

    new = -1
    while low <= high:
        mid = (low + high) // 2
      
        if alist[mid] == k:

            new = mid
            high = mid - 1
    
            
            
        else:
            if alist[mid] < k:
                low = mid + 1
              
            else:
                high = mid - 1
    return new


def LastBinarySearch(alist, k):
    low = 0
    high  = len(alist) -1

    new = -1
    while low <= high:
        mid = (low + high) // 2
      
        if alist[mid] == k:

            new = mid
            low = mid + 1
    
            
            
        else:
            if alist[mid] < k:
                low = mid + 1
              
            else:
                high = mid - 1
    return new
alist = [1,26,99,99,178,198,200,187]
k = 98
print (FirstBinarySearch(alist, k), LastBinarySearch(alist, k))
