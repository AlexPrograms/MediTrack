from abc import ABC, abstractmethod
import random


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
        data = data[:]
        if len(data) <= 1:
            return data
        pivot = data[0]
        lesser = [item for item in data[1:] if key_func(item) <= key_func(pivot)]
        greater = [item for item in data[1:] if key_func(item) > key_func(pivot)]
        return self.sort(lesser, key_func) + [pivot] + self.sort(greater, key_func)


class HeapSort(SortStrategy):
    """Implements Heap Sort algorithm."""

    def sort(self, data, key_func):
        data = data[:]
        total_elements = len(data)

        # Build max heap
        for current_index in range(total_elements // 2 - 1, -1, -1):
            self.heapify(data, total_elements, current_index, key_func)

        # Extract elements one by one
        for end_index in range(total_elements - 1, 0, -1):
            data[0], data[end_index] = data[end_index], data[0]
            self.heapify(data, end_index, 0, key_func)

        return data

    def heapify(self, data, heap_size, root_index, key_func):
        largest_index = root_index
        left_child_index = 2 * root_index + 1
        right_child_index = 2 * root_index + 2

        # Compare using key_func
        if (left_child_index < heap_size and
                key_func(data[left_child_index]) > key_func(data[largest_index])):
            largest_index = left_child_index

        if (right_child_index < heap_size and
                key_func(data[right_child_index]) > key_func(data[largest_index])):
            largest_index = right_child_index

        if largest_index != root_index:
            data[root_index], data[largest_index] = data[largest_index], data[root_index]
            self.heapify(data, heap_size, largest_index, key_func)


class MergeSort(SortStrategy):
    """Implements Merge Sort algorithm."""

    def sort(self, data, key_func):
        data = data[:]
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

#Fun algorithms
class Bogosort(SortStrategy):
    """Implements Bogosort Sort algorithm."""

    def sort(self, data, key_func):
        data = data[:]

        def is_sorted(arr):
            return all(key_func(arr[i]) <= key_func(arr[i + 1]) for i in range(len(arr) - 1))

        while not is_sorted(data):
            random.shuffle(data)
        return data

class Gnomesort(SortStrategy):
    """Implements Gnomesort Sort algorithm."""

    def sort(self, data, key_func):
        data = data[:]
        pos = 0
        while pos < len(data):
            if pos == 0 or key_func(data[pos]) >= key_func(data[pos - 1]):
                pos += 1
            else:
                data[pos], data[pos - 1] = data[pos - 1], data[pos]
                pos -= 1
        return data



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

if __name__ == '__main__':
    data = [4, 2, 9, 1, 5, 6]
    context = SortContext(HeapSort())
    sorted_data = context.execute_sort(data, key_func=lambda x: x)
    print(sorted_data)