import HeapSort
import collections
from QuickSort import quick_sort
from CountSort import count_sort


def test_priority_queue_init():
    data = [1, 2, 5, 6, 4, 3]
    queue = HeapSort.PriorityQueue(data)
    assert is_heap_invarient(queue._heap.get_heap())


def test_priority_queue_extract_max():
    data = [1, 2, 5, 6, 4, 3]
    queue = HeapSort.PriorityQueue(data)
    assert queue.extract_max() == 6
    assert len(queue._heap.get_heap()) == 5
    assert collections.Counter([1, 2, 3, 4, 5]) == collections.Counter(queue._heap.get_heap())
    assert is_heap_invarient(queue._heap.get_heap())


def test_increse_key():
    data = [1, 2, 5, 6, 4, 3]
    queue = HeapSort.PriorityQueue(data)
    queue.increse_key(3, 7)
    assert collections.Counter([1, 7, 3, 4, 5, 6]) == collections.Counter(queue._heap.get_heap())
    assert is_heap_invarient(queue._heap.get_heap())


def test_quick_sort():
    data = [1, 2, 5, 6, 4, 3]
    quick_sort(data)
    assert(data == [1, 2, 3, 4, 5, 6])


def is_heap_invarient(heap):
    for num in range(len(heap) // 2):
        if (num) * 2 < len(heap):
            if not heap[num] > heap[(num + 1) * 2 - 1]:
                return False
        if num * 2 + 1 < len(heap):
            if not heap[num] > heap[(num + 1) * 2 - 1]:
                return False
        return True


def test_count_sort_empty():
    assert count_sort([]) == []


def test_count_sort_one_item():
    assert count_sort([1]) == [1]


def test_count_sort_many_same_items():
    assert count_sort([4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 4) == [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]


def test_count_sort_many_items_ordered():
    assert count_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_count_sort_many_items_unordered():
    array = [2, 5, 76, 4, 7, 8, 43, 4, 4, 4, 4, 1, 0, 2, 2, 34]
    assert count_sort(array, 76) == sorted(array)
