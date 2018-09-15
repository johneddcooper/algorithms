from CalculateRunTime import calculateRunTime
import random
from MergeSort import merge_sort
from insertion_sort import insertion_sort
from HeapSort import heap_sort

merge_times = []
insertion_times = []
sorted_times = []
heap_times = []

for i in range(20):
    sample = random.sample(range(10000), 900)
    sorted_results = calculateRunTime(sorted, sample)
    sorted_times.append(sorted_results[0])

    #merge_results = calculateRunTime(merge_sort, sample)
    #insertion_results = calculateRunTime(insertion_sort, sample)
    heap_results = calculateRunTime(heap_sort, sample)

    # if merge_results[1] != sorted_results[1]:
    #     raise Exception("Merge error:", merge_results[1])
    # if insertion_results[1] != sorted_results[1]:
    #     raise Exception("Insertion error:", insertion_results[1])
    if heap_results[1] != sorted_results[1]:
        raise Exception("Heap error:", heap_results[1])

    # merge_times.append(merge_results[0])
    # insertion_times.append(insertion_results[0])
    heap_times.append(heap_results[0])


# print("merge:", sum(merge_times) / len(merge_times))
#print("insert:", sum(insertion_times) / len(insertion_times))
print("sorted:", sum(sorted_times) / len(sorted_times))
print("heap:", sum(heap_times) / len(heap_times))
