import HeapSort
import collections


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


def test_priority_queue_insert():
    data = [1, 5, 6, 4, 3]
    queue = HeapSort.PriorityQueue(data)
    queue.insert(8)
    queue.insert(2)
    assert collections.Counter([1, 2, 3, 4, 5, 6, 8]) == collections.Counter(queue._heap.get_heap())
    assert is_heap_invarient(queue._heap.get_heap())


def is_heap_invarient(heap):
    for num in range(len(heap) // 2):
        if (num) * 2 < len(heap):
            if not heap[num] > heap[(num + 1) * 2 - 1]:
                return False
        if num * 2 + 1 < len(heap):
            if not heap[num] > heap[(num + 1) * 2 - 1]:
                return False
        return True
