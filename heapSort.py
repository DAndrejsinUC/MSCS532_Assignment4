import random
from time import time


def heapify(arr, n, i):
    """
    Maintain the max heap property for a subtree rooted at index i.
    
    Args:
        arr: The array being heapified
        n: Size of the heap
        i: Root index of the subtree
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # Compare with left child
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Compare with right child
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)

def build_max_heap(arr):
    """
    Build a max heap from an unsorted array.
    
    Args:
        arr: The array to be converted into a max heap
    """
    n = len(arr)
    # Start from last non-leaf node and heapify each node
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

def heap_sort(arr):
    """
    Sort an array using heapsort algorithm.
    
    Args:
        arr: The array to be sorted
    Returns:
        The sorted array
    """
    # Build max heap
    build_max_heap(arr)
    
    # Extract elements from heap one by one
    for i in range(len(arr) - 1, 0, -1):
        # Move current root (maximum element) to end
        arr[0], arr[i] = arr[i], arr[0]
        # Call max heapify on the reduced heap
        heapify(arr, i, 0)
    
    return arr

def generate_number_list(n: int, list_type: str) -> list:
    """
    Generate a list of n numbers based on the specified type.
    
    Args:
        n (int): The number of elements to generate
        list_type (str): Type of list to generate ('ascending', 'descending', 'random', or 'duplicates')
        
    Returns:
        list: Generated list of numbers
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
        
    if list_type.lower() not in ['ascending', 'descending', 'random']:
        raise ValueError("list_type must be 'ascending', 'descending', or 'random'")
    
    if list_type.lower() == 'ascending':
        return list(range(1, n + 1))
    elif list_type.lower() == 'descending':
        return list(range(n, 0, -1))
    else:  # random
        return random.sample(range(1, n * 2), n)  # Using n*2 to have a wider range of numbers

if __name__ == "__main__":
    list_ascending = generate_number_list(1000000, 'ascending')
    list_descending = generate_number_list(1000000, 'descending')
    list_random = generate_number_list(1000000, 'random')
    
    # Timing heap sort on each list
    print("Sorting ascending list with heap sort...")
    start = time()
    sorted_asc = heap_sort(list_ascending.copy())
    elapsed = time() - start
    print(f"Elapsed time: {elapsed:.6f} seconds")

    print("Sorting descending list with heap sort...")
    start = time()
    sorted_desc = heap_sort(list_descending.copy())
    elapsed = time() - start
    print(f"Elapsed time: {elapsed:.6f} seconds")

    print("Sorting random list with heap sort...")
    start = time()
    sorted_rand = heap_sort(list_random.copy())
    elapsed = time() - start
    print(f"Elapsed time: {elapsed:.6f} seconds")