"""
Kadane's Algorithm - Maximum Subarray Problem
Finds the contiguous subarray with the largest sum in O(n) time
"""

def kadanes_algorithm(arr):
    """
    Find the maximum sum of any contiguous subarray using Kadane's algorithm.
    
    Args:
        arr (list): List of integers (positive and/or negative)
    
    Returns:
        tuple: (max_sum, start_index, end_index, max_subarray)
    """
    
    if not arr:
        return 0, 0, 0, []
    
    # Initialize variables
    max_sum = arr[0]           # Overall maximum sum found so far
    current_sum = arr[0]       # Maximum sum ending at current position
    start = 0                  # Start index of max subarray
    end = 0                    # End index of max subarray
    temp_start = 0             # Temporary start for current subarray
    
    # Iterate through array starting from index 1
    for i in range(1, len(arr)):
        # Decision point: extend current subarray or start fresh
        if current_sum < 0:
            current_sum = arr[i]
            temp_start = i
        else:
            current_sum += arr[i]
        
        # Update max_sum if current_sum is larger
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
    
    max_subarray = arr[start:end+1]
    return max_sum, start, end, max_subarray


def kadanes_algorithm_modified(arr):
    """
    Modified version that also handles all-negative arrays and returns indices.
    """
    if not arr:
        return None
    
    max_sum = arr[0]
    current_sum = arr[0]
    start = 0
    end = 0
    temp_start = 0
    
    for i in range(1, len(arr)):
        # If adding current element gives better result
        if current_sum + arr[i] > arr[i]:
            current_sum += arr[i]
        else:
            current_sum = arr[i]
            temp_start = i
        
        # Update if better solution found
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
    
    return {
        "max_sum": max_sum,
        "start_index": start,
        "end_index": end,
        "subarray": arr[start:end+1]
    }


# Test Cases
if __name__ == "__main__":
    print("=" * 60)
    print("KADANE'S ALGORITHM - MAXIMUM SUBARRAY PROBLEM")
    print("=" * 60)
    
    test_cases = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        [-13, -3, -25, -20, -3, -16, -23, -12, -5, -27, -30, -6, -28, -15, -4, -17, -8, -11, -26, -14, -1, -5, -24, -10, -16, -9, -10, -32, -21, -50],
        [5, -3, 5],
        [-2, -3, 4, -1, -2, 1, 5, -3],
        [1, 2, 3, 4, 5],
        [-5, -2, -8, -1, -4]
    ]
    
    for i, arr in enumerate(test_cases, 1):
        print(f"\nTest Case {i}: {arr}")
        max_sum, start, end, subarray = kadanes_algorithm(arr)
        print(f"Maximum Sum: {max_sum}")
        print(f"Subarray: {subarray}")
        print(f"Range: indices [{start}, {end}]")
        print("-" * 60)
