from abc import ABC, abstractmethod

from django.template.defaultfilters import length


class SortStrategy(ABC):
    """Abstract base class for sorting strategies."""

    @abstractmethod
    def sort(self, data, key_func):
        pass


class BubbleSort(SortStrategy):
    """Implements Bubble Sort algorithm."""

    def sort(self, data, key_func):
        data = data[:]  # Make a copy to avoid modifying the original list
        n = len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if key_func(data[j]) > key_func(data[j + 1]):
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data


class QuickSort(SortStrategy):
    """Implements Quick Sort algorithm."""

    def sort(self, data, key_func):
        data = data[:]  # Make a copy to avoid modifying the original list
        if len(data) <= 1:
            return data
        pivot = data[0]
        lesser = [item for item in data[1:] if key_func(item) <= key_func(pivot)]
        greater = [item for item in data[1:] if key_func(item) > key_func(pivot)]
        return self.sort(lesser, key_func) + [pivot] + self.sort(greater, key_func)



class HeapSort(SortStrategy):
    """Implements Heap Sort algorithm."""

    def sort(self, data, key_func):
        data = data[:]  # Make a copy to avoid modifying the original list

        return data



class MergeSort(SortStrategy):
    """Implements Merge Sort algorithm."""

    def sort(self, data, key_func):
        data = data[:]  # Make a copy to avoid modifying the original list
        if len(data) <= 1:
            return data

        middle = len(data) // 2
        left = data[:middle]
        right = data[middle:]

        left_sorted = self.sort(left, key_func)
        right_sorted = self.sort(right, key_func)

        return self.merge(left_sorted, right_sorted, key_func)

    def merge(self, left, right, key_func):
        result = []
        l = r = 0

        while l < len(left) and r < len(right):
            if key_func(left[l]) <= key_func(right[r]):
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1

        result.extend(left[l:])
        result.extend(right[r:])
        return result






class SortContext:
    """Context class to apply different sorting strategies."""

    def __init__(self, strategy: SortStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: SortStrategy):
        """Dynamically change the sorting strategy."""
        self.strategy = strategy

    def execute_sort(self, data, key_func):
        """Sort the data using the selected strategy."""
        return self.strategy.sort(data, key_func)

# if __name__ == '__main__':
#     data = [4, 2, 9, 1, 5, 6]
#     context = SortContext(MergeSort())
#     sorted_data = context.execute_sort(data, key_func=lambda x: x)
#     print(sorted_data)