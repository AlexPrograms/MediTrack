def bubble_sort(objects, key_func):
    """Sorts a list using Bubble Sort based on a given key function."""
    n = len(objects)
    for i in range(n):
        for j in range(0, n - i - 1):
            if key_func(objects[j]) > key_func(objects[j + 1]):
                objects[j], objects[j + 1] = objects[j + 1], objects[j]
    return objects


def quick_sort(objects, key_func):
    """Sorts a list using Quick Sort based on a given key function."""
    if len(objects) <= 1:
        return objects

    pivot = key_func(objects[len(objects) // 2])
    left = [x for x in objects if key_func(x) < pivot]
    middle = [x for x in objects if key_func(x) == pivot]
    right = [x for x in objects if key_func(x) > pivot]

    return quick_sort(left, key_func) + middle + quick_sort(right, key_func)


def filter_appointments(appointments, status=None, date_range=None):
    """Filters appointments based on status and date range."""
    if status:
        appointments = [appt for appt in appointments if appt.status == status]
    if date_range:
        start, end = date_range
        appointments = [appt for appt in appointments if start <= appt.date <= end]
    return appointments
