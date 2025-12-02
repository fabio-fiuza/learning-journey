from time import perf_counter_ns

def insertion_sort(arr: list[int]) -> list[int]:
    """
    Sorts a list of integers using the Insertion Sort algorithm.
    
    Args:
        arr (list[int]): List of integers to be sorted.
        
    Returns:
        list[int]: The sorted list.
        
    Observations:
    - Time Complexity: O(n^2) in the worst case, O(n) in the best case.
    - Space Complexity: O(1)
    - Stable: Yes
    - In-Place: Yes
    """
    array_size = len(arr)
    
    for i in range(1, array_size):
        
        key = arr[i] 
        j = i - 1     
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key
        
    return arr

if __name__ == "__main__":
    
    worst_case_unsorted_list = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
    
    unsorted_list = worst_case_unsorted_list.copy()
    
    start_time = perf_counter_ns()
    sorted_list = insertion_sort(unsorted_list)
    end_time = perf_counter_ns()
    
    insertion_sort_time = end_time - start_time
    
    print(f"Insertion Sort Result: {sorted_list}")
    print(f"Insertion Sort Time: {insertion_sort_time} ns")