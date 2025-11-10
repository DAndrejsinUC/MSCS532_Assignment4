# MSCS532_Assignment4

This repository contains two implementations:
1. A Heap Sort algorithm
2. A Priority Queue using a max-heap

## Running Heap Sort (heapSort.py)

To run the heap sort implementation:

```bash
python heapSort.py
```

This will run tests on three different types of lists (1 million elements each):
- Ascending order list
- Descending order list
- Random order list

The program will display the time taken to sort each list type.

## Running Priority Queue (priorityQueue.py)

To run the priority queue implementation:

```bash
python priorityQueue.py
```

This will demonstrate the priority queue operations:
1. Insert three tasks with different priorities
2. Increase the priority of the lowest priority task
3. Extract all tasks in priority order (highest priority first)

Each operation will print its results to show how the priority queue is working.

## Expected Output

### HeapSort
You will see timing results for sorting each type of list, showing how the algorithm performs with different input arrangements.

### Priority Queue
You will see:
- Tasks being inserted with their IDs and priorities
- A priority increase operation
- Tasks being extracted in order of highest to lowest priority