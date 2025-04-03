# """Bubble sort"""
# def Bsort(data):
#     data = data[:]
#     n = len(data)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if data[j] > data[j + 1]:
#                 print(data[j], data[j + 1])
#                 data[j], data[j + 1] = data[j + 1], data[j]
#     return data
#
# """Quick sort"""
# def Qsort(arr, low, high):
#     if low < high:
#         # pi is the partition return index of pivot
#         pi = partition(arr, low, high)
#
#         # Recursion calls for smaller elements
#         # and greater or equals elements
#         Qsort(arr, low, pi - 1)
#         Qsort(arr, pi + 1, high)
#
#
# # Partition function
# def partition(arr, low, high):
#     # Choose the pivot
#     pivot = arr[high]
#
#     # Index of smaller element and indicates
#     # the right position of pivot found so far
#     i = low - 1
#
#     # Traverse arr[low..high] and move all smaller
#     # elements to the left side. Elements from low to
#     # i are smaller after every iteration
#     for j in range(low, high):
#         if arr[j] < pivot:
#             i += 1
#             swap(arr, i, j)
#
#     # Move pivot after smaller elements and
#     swap(arr, i + 1, high)
#     # return its position
#     return i + 1
#
#
# # Swap function
# def swap(arr, i, j):
#     arr[i], arr[j] = arr[j], arr[i]
#
#
# if __name__ == "__main__":
#     arr = [64, 34, 25, 12, 22, 11, 90]
#
#     Bsort(arr)
#
#     print("Sorted array:")
#     for i in range(len(arr)):
#         print("%d" % arr[i], end=" ")
#
#     n = len(arr)
#
#     Qsort(arr, 0, n - 1)
#
#     for val in arr:
#         print(val, end=" ")


#Strategy
from abc import ABC, abstractmethod

# Step 1: Define the Strategy Interface
class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass

# Step 2: Implement Concrete Sorting Strategies

class BubbleSort(SortingStrategy):
    def sort(self, data):
        arr = data[:]  # Copy to avoid modifying the original list
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap
        return arr

class QuickSort(SortingStrategy):
    def sort(self, data):
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        print(pivot)
        left = [x for x in data if x < pivot]
        print(left)
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        print(right)
        return self.sort(left) + middle + self.sort(right)

# Step 3: Create a Context Class that Uses a Sorting Strategy
class SortContext:
    def __init__(self, strategy: SortingStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: SortingStrategy):
        """Allows changing the sorting strategy at runtime."""
        self.strategy = strategy

    def execute_sort(self, data):
        return self.strategy.sort(data)

# Step 4: Test the Strategy Pattern Implementation
data = [64, 34, 25, 12, 22, 11, 90]
print(data)

# Using Bubble Sort
context = SortContext(BubbleSort())
print("Bubble Sort:", context.execute_sort(data))

# Switching to Quick Sort
context.set_strategy(QuickSort())
print("Quick Sort:", context.execute_sort(data))
