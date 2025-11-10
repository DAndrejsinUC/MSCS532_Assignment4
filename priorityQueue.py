from dataclasses import dataclass
from typing import Optional
import time

@dataclass
class Task:
    """
    Class to represent a task with priority and other relevant information.
    Using max-heap, so higher priority values indicate more important tasks.
    """
    task_id: int
    priority: int
    arrival_time: float
    deadline: Optional[float] = None
    description: str = ""

    def __lt__(self, other):
        # For comparison in heap operations
        return self.priority < other.priority

class PriorityQueue:
    """
    Priority Queue implementation using a max-heap.
    We use a list-based implementation for the heap as it provides:
    1. O(1) random access for parent/child relationships
    2. Dynamic resizing handled by Python
    3. Cache-friendly contiguous memory storage
    4. Built-in methods for appending and popping
    """
    def __init__(self):
        # Using list for heap implementation starting with index 0
        # For any node at index i:
        # - Parent is at (i-1)//2
        # - Left child is at 2*i + 1
        # - Right child is at 2*i + 2
        self._heap = []
        self._task_positions = {}  # Maps task_id to its position in heap

    def _parent(self, index: int) -> int:
        """Get parent index"""
        return (index - 1) // 2

    def _left_child(self, index: int) -> int:
        """Get left child index"""
        return 2 * index + 1

    def _right_child(self, index: int) -> int:
        """Get right child index"""
        return 2 * index + 2

    def _swap(self, i: int, j: int):
        """Swap elements at indices i and j, updating task positions"""
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]
        self._task_positions[self._heap[i].task_id] = i
        self._task_positions[self._heap[j].task_id] = j

    def _sift_up(self, index: int):
        """
        Move a node up in the heap until heap property is restored.
        Time Complexity: O(log n)
        """
        parent = self._parent(index)
        if index > 0 and self._heap[index].priority > self._heap[parent].priority:
            self._swap(index, parent)
            self._sift_up(parent)

    def _sift_down(self, index: int):
        """
        Move a node down in the heap until heap property is restored.
        Time Complexity: O(log n)
        """
        largest = index
        left = self._left_child(index)
        right = self._right_child(index)
        size = len(self._heap)

        if left < size and self._heap[left].priority > self._heap[largest].priority:
            largest = left

        if right < size and self._heap[right].priority > self._heap[largest].priority:
            largest = right

        if largest != index:
            self._swap(index, largest)
            self._sift_down(largest)

    def insert(self, task: Task):
        """
        Insert a new task into the priority queue.
        Time Complexity: O(log n)
        """
        self._heap.append(task)
        index = len(self._heap) - 1
        self._task_positions[task.task_id] = index
        self._sift_up(index)

    def extract_max(self) -> Optional[Task]:
        """
        Remove and return the highest priority task.
        Time Complexity: O(log n)
        """
        if self.is_empty():
            return None

        self._swap(0, len(self._heap) - 1)
        max_task = self._heap.pop()
        del self._task_positions[max_task.task_id]

        if self._heap:
            self._sift_down(0)

        return max_task

    def increase_key(self, task_id: int, new_priority: int):
        """
        Increase the priority of a task.
        Time Complexity: O(log n)
        """
        if task_id not in self._task_positions:
            raise ValueError("Task not found in queue")

        index = self._task_positions[task_id]
        if new_priority < self._heap[index].priority:
            raise ValueError("New priority is less than current priority")

        self._heap[index].priority = new_priority
        self._sift_up(index)

    def decrease_key(self, task_id: int, new_priority: int):
        """
        Decrease the priority of a task.
        Time Complexity: O(log n)
        """
        if task_id not in self._task_positions:
            raise ValueError("Task not found in queue")

        index = self._task_positions[task_id]
        if new_priority > self._heap[index].priority:
            raise ValueError("New priority is greater than current priority")

        self._heap[index].priority = new_priority
        self._sift_down(index)

    def is_empty(self) -> bool:
        """
        Check if the priority queue is empty.
        Time Complexity: O(1)
        """
        return len(self._heap) == 0

    def __len__(self) -> int:
        """Return the number of tasks in the queue"""
        return len(self._heap)


# Example usage and testing
if __name__ == "__main__":
    # Create a priority queue
    pq = PriorityQueue()

    # Create some test tasks
    tasks = [
        Task(1, 3, time.time(), time.time() + 3600, "Low priority task"),
        Task(2, 7, time.time(), time.time() + 1800, "High priority task"),
        Task(3, 5, time.time(), time.time() + 2400, "Medium priority task"),
    ]

    # Insert tasks
    print("Inserting tasks...")
    for task in tasks:
        pq.insert(task)
        print(f"Inserted Task {task.task_id} with priority {task.priority}")

    # Test increase_key
    print("\nIncreasing priority of Task 1 from 3 to 8...")
    pq.increase_key(1, 8)

    # Extract tasks in priority order
    print("\nExtracting tasks in priority order:")
    while not pq.is_empty():
        task = pq.extract_max()
        print(f"Task {task.task_id} (Priority: {task.priority})")
