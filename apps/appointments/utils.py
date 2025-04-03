# def bubble_sort(objects, key_func):
#     """Sorts a list using Bubble Sort based on a given key function."""
#     n = len(objects)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if key_func(objects[j]) > key_func(objects[j + 1]):
#                 objects[j], objects[j + 1] = objects[j + 1], objects[j]
#     return objects
#
#
# def quick_sort(objects, key_func):
#     """Sorts a list using Quick Sort based on a given key function."""
#     if len(objects) <= 1:
#         return objects
#
#     pivot = key_func(objects[len(objects) // 2])
#     left = [x for x in objects if key_func(x) < pivot]
#     middle = [x for x in objects if key_func(x) == pivot]
#     right = [x for x in objects if key_func(x) > pivot]
#
#     return quick_sort(left, key_func) + middle + quick_sort(right, key_func)
#
#
# def filter_appointments(appointments, status=None, date_range=None):
#     """Filters appointments based on status and date range."""
#     if status:
#         appointments = [appt for appt in appointments if appt.status == status]
#     if date_range:
#         start, end = date_range
#         appointments = [appt for appt in appointments if start <= appt.date <= end]
#     return appointments


#Strategy design pattern for sorting
from abc import ABC, abstractmethod

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass

class BubbleSort(SortStrategy):
    def sort(self, data):
        data = data.copy()
        n = len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data

class QuickSort(SortStrategy):
    def sort(self, data):
        data = data[:]
        if len(data) <= 1:
            return data
        else:
            pivot = data.pop(0)
            greater = []
            lesser = []
            for item in data:
                if item > pivot:
                    greater.append(item)
                else:
                    lesser.append(item)
            return self.sort(lesser) + [pivot] + self.sort(greater)

class SortContext:
    def __init__(self, strategy: SortStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: SortStrategy):
        """Change the sorting strategy dynamically."""
        self.strategy = strategy

    def execute_sort(self, data):
        return self.strategy.sort(data)


if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]

    # Using Bubble Sort
    context = SortContext(BubbleSort())
    print("Bubble Sort:", context.execute_sort(data))

    # Switching to Quick Sort
    context.set_strategy(QuickSort())
    print("Quick Sort:", context.execute_sort(data))
