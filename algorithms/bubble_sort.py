from typing import Literal
from time import perf_counter_ns

def _bubble_sort_runner(arr: list[int], stop_early: bool) -> None:
    
    """
    Implements the bubble sort algorithm.
    
    Parameters:
    - arr: List of integers to be sorted.
    - stop_early: If True, the algorithm will stop early if no swaps are made in a pass.
    
    """
    
    arr_size = len(arr)
    
    for i in range(arr_size):
        swapped = False
        
        for j in range(0, arr_size - i - 1):
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
                swapped = True
        
        if stop_early and not swapped:
            break

def bubble_sort(arr: list[int], method: Literal['classic', 'optimized'] = 'classic') -> list[int]:
    
    """
    Sorts a list of integers using the bubble sort algorithm.
    
    Parameters:
    - arr: List of integers to be sorted.
    - method: 'classic' for standard bubble sort, 'optimized' for early stopping if no swaps occur.
    
    Returns:
    - The sorted list of integers.
    """
   
    if method not in ["classic", "optimized"]:
        raise ValueError("Method must be 'classic' or 'optimized'")
    
    should_stop_early = (method == "optimized")
    
    _bubble_sort_runner(arr, stop_early=should_stop_early)
    
    return arr

if __name__ == "__main__":
    
    worst_case_ursorted_list = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
    
    unsorted_list_1 = worst_case_ursorted_list.copy()
    unsorted_list_2 = worst_case_ursorted_list.copy()
    
    start_time = perf_counter_ns()
    sorted_list_1 = bubble_sort(unsorted_list_1, method="classic")
    end_time = perf_counter_ns()
    
    classic_bubble_sort_time = end_time - start_time
    
    print(f"Classic Bubble Sort Result: {sorted_list_1}")
    print(f"Classic Bubble Sort Time: {classic_bubble_sort_time} ns")
    
    start_time = perf_counter_ns()
    sorted_list_2 = bubble_sort(unsorted_list_2, method="optimized")
    end_time = perf_counter_ns()
    
    optimized_bubble_sort_time = end_time - start_time
    print(f"Optimized Bubble Sort Result: {sorted_list_2}")
    print(f"Optimized Bubble Sort Time: {optimized_bubble_sort_time} ns")
    
    print(f"Time Difference: {classic_bubble_sort_time - optimized_bubble_sort_time} ns")
    
    