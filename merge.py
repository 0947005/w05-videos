def merge(arr1, arr2):
    '''
    Merge 2 sorted lists into one sorted list.
    
    Input:
        arr1 (list): sorted list
        arr2 (list): sorted list
    
    Output:
        sorted_list (list): the lists arr1 and arr2 combined in sorted order.
    
    Examples:
    >>> merge([1, 2, 3], [4, 5, 6])
    [1, 2, 3, 4, 5, 6]
    
    >>> merge([1, 2], [1, 2])
    [1, 1, 2, 2]
    '''
    sorted_list = []

    # Loop until the full list is formed, start at index 0 for both lists
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        # Compare the items at the current locations for both lists
        if arr1[i] < arr2[j]:
            sorted_list.append(arr1[i])
            i += 1
        else:
            sorted_list.append(arr2[j])
            j += 1

    # Add any remaining elements in arr1 or arr2 to the end
    sorted_list.extend(arr1[i:])
    sorted_list.extend(arr2[j:])
    return sorted_list

import doctest
doctest.testmod()