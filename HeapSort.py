def _left(i):
    return 2 * i


def _right(i):
    return 2 * i + 1


def _parent(i):
    return i // 2


def _max_heapify(heap, parent_index):
    left_child_index = _left(parent_index)
    right_child_index = _right(parent_index)
    largest_index = parent_index
    if left_child_index <= heap.heap_size - 1 and heap[left_child_index] > heap[parent_index]:
        largest_index = left_child_index
    if right_child_index <= heap.heap_size - 1 and heap[right_child_index] > heap[largest_index]:
        largest_index = right_child_index
    if largest_index != parent_index:
        heap[parent_index], heap[largest_index] = heap[largest_index], heap[parent_index]
        _max_heapify(heap, largest_index)


def _build_max_heap(heap):
    heap.heap_size = len(heap)
    for i in range(heap.heap_size - 1 // 2, -1, -1):
        _max_heapify(heap, i)


class _Heap:
    def __init__(self, array):
        self.heap_size = 0
        self.heap_array = array

    def __len__(self):
        return len(self.heap_array)

    def __getitem__(self, key):
        return self.heap_array[key]

    def __setitem__(self, key, value):
        self.heap_array[key] = value

    def get_max(self):
        return self.heap_array[0]

    def get_heap(self):
        return self.heap_array[:self.heap_size]

    def increse_key(self, index, key):
        if key < self.heap_array[index]:
            return Exception("New key is smaller than old key")

        self.heap_array[index] = key
        while index > 0 and self.heap_array[_parent(index)] < self.heap_array[index]:
            self.heap_array[_parent(index)], self.heap_array[index] = self.heap_array[index], self.heap_array[_parent(index)]
            index = _parent(index)


class _SortedHeap(_Heap):
    def __init__(self, array=None):
        self.heap_size = 0
        self.heap_array = array
        if self.heap_array:
            self._sort()

    def _sort(self):
        _build_max_heap(self)
        # for i in range(len(self) - 1, 0, -1):
        #     self[0], self[i] = self[i], self[0]
        #     self.heap_size -= 1
        #     _max_heapify(self, 0)


def heap_sort(array):
    heap = _SortedHeap(array)
    #_build_max_heap(heap)
    # for i in range(len(heap) - 1, 0, -1):
    #     heap[0], heap[i] = heap[i], heap[0]
    #     heap.heap_size -= 1
    #     _max_heapify(heap, 0)
    return heap.heap_array


class PriorityQueue:

    def __init__(self, data=None):
        self._heap = _SortedHeap(data)

    def get_max(self):
        return self._heap.get_max()

    def extract_max(self):
        if len(self._heap) < 1:
            return IndexError("Heap Empty")
        max_value = self._heap.get_max()
        self._heap.heap_size -= 1
        self._heap[0] = self._heap[self._heap.heap_size]
        _max_heapify(self._heap, 0)
        return max_value

    def increse_key(self, key, index):
        self._heap.increse_key(key, index)

    def insert(self, key):
        self._heap.heap_size += 1
        self._heap.heap_array.append(key)
        self._heap.increse_key(self._heap.heap_size - 1, key)
