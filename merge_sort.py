"""
Merge Sort Algorithm
Divide and Conquer sorting approach - Guaranteed O(n log n)
Time Complexity: O(n log n) in all cases
Space Complexity: O(n) for auxiliary arrays
Stable Sort: Yes
"""

def merge_sort(arr):
    """
    Merge Sort using divide and conquer approach.
    
    Args:
        arr (list): List of elements to sort
    
    Returns:
        list: Sorted list
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)


def merge(left, right):
    """
    Merge two sorted arrays into one sorted array.
    
    Args:
        left (list): First sorted list
        right (list): Second sorted list
    
    Returns:
        list: Merged sorted list
    """
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


def merge_sort_inplace(arr, left=0, right=None):
    """
    In-place Merge Sort with auxiliary array.
    
    Args:
        arr (list): List to sort
        left (int): Starting index
        right (int): Ending index
    
    Returns:
        list: Sorted list (modified in-place)
    """
    if right is None:
        right = len(arr) - 1
    
    if left < right:
        mid = (left + right) // 2
        merge_sort_inplace(arr, left, mid)
        merge_sort_inplace(arr, mid + 1, right)
        merge_inplace(arr, left, mid, right)
    
    return arr


def merge_inplace(arr, left, mid, right):
    """
    Merge subarrays in-place for in-place merge sort.
    """
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]
    
    i = j = 0
    k = left
    
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1
    
    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1
    
    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1


def merge_sort_with_count(arr):
    """
    Merge Sort that also counts inversions.
    An inversion is a pair (i, j) where i < j but arr[i] > arr[j].
    
    Returns:
        tuple: (sorted_array, inversion_count)
    """
    def merge_count(left, right):
        result = []
        inversions = 0
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                inversions += len(left) - i
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        
        return result, inversions
    
    def sort_count(arr):
        if len(arr) <= 1:
            return arr, 0
        
        mid = len(arr) // 2
        left, left_inv = sort_count(arr[:mid])
        right, right_inv = sort_count(arr[mid:])
        merged, split_inv = merge_count(left, right)
        
        return merged, left_inv + right_inv + split_inv
    
    sorted_arr, inversions = sort_count(arr)
    return sorted_arr, inversions


# Test Cases
if __name__ == "__main__":
    print("=" * 60)
    print("MERGE SORT ALGORITHM TESTS")
    print("=" * 60)
    
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 8, 1, 9],
        [1],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [3, 3, 3, 3, 3]
    ]
    
    for i, arr in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print(f"Original: {arr}")
        
        # Standard merge sort
        sorted_arr = merge_sort(arr.copy())
        print(f"Sorted: {sorted_arr}")
        
        # In-place merge sort
        arr_copy = arr.copy()
        merge_sort_inplace(arr_copy)
        print(f"Sorted (In-place): {arr_copy}")
        
        # Merge sort with inversion count
        sorted_arr, inversions = merge_sort_with_count(arr.copy())
        print(f"Inversions: {inversions}")
        
        print("-" * 60)
