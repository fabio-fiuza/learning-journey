from time import perf_counter_ns

def selection_sort(arr: list[int]) -> list[int]:
    """
    Sorts a list of integers using the selection sort algorithm.
    
    Parameters:
    - arr: List of integers to be sorted.
    
    Returns:
    - The sorted list of integers.
    
    Observations:
    - Time Complexity: O(n^2) in all cases.
    - Space Complexity: O(1)
    - Stable: No
    - In-Place: Yes
    """
    
    arr_size = len(arr)
    
    for i in range(arr_size):
        min_index = i
        
        for j in range(i + 1, arr_size):
            
            if arr[j] < arr[min_index]:
                min_index = j
        
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

if __name__ == "__main__":
    
    worst_case_unsorted_list = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
    
    unsorted_list = worst_case_unsorted_list.copy()
    
    start_time = perf_counter_ns()
    sorted_list = selection_sort(unsorted_list)
    end_time = perf_counter_ns()
    
    selection_sort_time = end_time - start_time
    
    print(f"Selection Sort Time: {selection_sort_time} ns")