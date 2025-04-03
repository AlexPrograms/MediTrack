from abc import ABC, abstractmethod


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
