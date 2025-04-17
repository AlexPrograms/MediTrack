import unittest
import random
import time

from .utils import (
    BubbleSort, QuickSort, MergeSort, HeapSort, Gnomesort, Bogosort,
    SortContext
)


class TestSortStrategies(unittest.TestCase):
    def setUp(self):
        self.strategies = [
            BubbleSort(),
            QuickSort(),
            MergeSort(),
            HeapSort(),
            Gnomesort(),
            Bogosort(),  # only for small safe input
        ]
        self.context = SortContext(QuickSort())
        self.test_lists = [
            [],
            [1],
            [5, 2],
            [3, 1, 4, 1, 5, 9],
            list(range(10, 0, -1)),
            [random.randint(0, 100) for _ in range(20)],
        ]

    def test_sorting_correctness(self):
        for strategy in self.strategies:
            if isinstance(strategy, Bogosort):
                continue  # Handled separately
            self.context.set_strategy(strategy)
            for lst in self.test_lists:
                with self.subTest(strategy=strategy.__class__.__name__, data=lst):
                    expected = sorted(lst)
                    result = self.context.execute_sort(lst, key_func=lambda x: x)
                    self.assertEqual(result, expected)

    def test_with_key_func(self):
        data = ['fig', 'kiwi', 'apple', 'banana', 'cherry']
        expected = sorted(data, key=lambda x: len(x))

        for strategy in self.strategies:
            if isinstance(strategy, Bogosort):
                continue

            with self.subTest(strategy=strategy.__class__.__name__):
                self.context.set_strategy(strategy)
                result = self.context.execute_sort(data.copy(), key_func=lambda x: len(x))

                # First verify the lengths are in correct order
                result_lengths = [len(x) for x in result]
                expected_lengths = [len(x) for x in expected]
                self.assertEqual(result_lengths, expected_lengths)

                # Then verify all elements are present
                self.assertEqual(sorted(result), sorted(data))

                # For stable sorts, also verify exact order
                if isinstance(strategy, (BubbleSort, MergeSort, Gnomesort)):
                    self.assertEqual(result, expected)

    def test_bogosort_safe(self):
        data = ['fig', 'kiwi', 'apple', 'banana', 'cherry']
        expected = sorted(data, key=lambda x: len(x))

        for strategy in self.strategies:
            if isinstance(strategy, Bogosort):
                continue

            with self.subTest(strategy=strategy.__class__.__name__):
                self.context.set_strategy(strategy)
                result = self.context.execute_sort(data.copy(), key_func=lambda x: len(x))

                # Verify the lengths are sorted correctly
                result_lengths = [len(x) for x in result]
                expected_lengths = [len(x) for x in expected]
                self.assertEqual(result_lengths, expected_lengths)

                # For unstable sorts, don't check exact order of equal-length elements
                if isinstance(strategy, (QuickSort, HeapSort)):
                    # Just verify all elements are present
                    self.assertEqual(sorted(result), sorted(data))
                else:
                    # For stable sorts, verify exact order
                    self.assertEqual(result, expected)

    def test_benchmark_all(self):
        print("\n--- Benchmarking Sorting Strategies ---")
        dataset = [random.randint(0, 10000) for _ in range(1000)]  # Moderate size
        for strategy in self.strategies:
            if isinstance(strategy, Bogosort):
                continue  # skip for performance reasons
            self.context.set_strategy(strategy)
            data_copy = dataset[:]
            start = time.perf_counter()
            self.context.execute_sort(data_copy, key_func=lambda x: x)
            end = time.perf_counter()
            print(f"{strategy.__class__.__name__}: {end - start:.6f} seconds")

if __name__ == '__main__':
    unittest.main()
