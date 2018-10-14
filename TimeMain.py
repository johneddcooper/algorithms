from CalculateRunTime import calculateRunTime
import random
from MergeSort import merge_sort
from insertion_sort import insertion_sort
from HeapSort import heap_sort_low
from QuickSort import quick_sort
from QuickSort import random_quick_sort
from CountSort import count_sort


class RandomArrayGenerator():
    def __init__(self, population_size, sample_size):
        self.population_size = population_size
        self.sample_size = sample_size

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        return random.sample(range(self.population_size), self.sample_size)


class ResultManager:
    def __init__(self):
        self.time_map = {}
        self.algorithm_map = {}

    def add_algorithm(self, algorithm_str, algorithm_func):
        self.algorithm_map[algorithm_str] = algorithm_func
        self.time_map[algorithm_str] = []

    def append_run_time(self, algorithm_str, runtime):
        self.time_map[algorithm_str].append(runtime)

    def run_serial(self, array, sorted_array=None):
        for algorithm_str, algorithm_func in self.algorithm_map.items():
            runtime, results = calculateRunTime(algorithm_func, array)
            if sorted_array and not results == sorted_array:
                raise Exception("Bad results:", algorithm_str, array, results, sorted_array)
            self.append_run_time(algorithm_str, runtime)

    def print_results(self):
        for algorithm_str, runtimes in self.time_map.items():
            ave_runtime = sum(runtimes) / len(runtimes)
            print(algorithm_str, ": ", ave_runtime)

    def run_test(self, serials=20, array_generator=RandomArrayGenerator(100, 100)):
        if len(self.algorithm_map) == 0:
            raise Exception("No algorithms added to test")
        for serial in range(serials):
            array = array_generator.next()
            self.run_serial(array, sorted(array))
        self.print_results()


max_value = 99999
result_manager = ResultManager()
result_manager.add_algorithm("sorted", sorted)
result_manager.add_algorithm("quick", quick_sort)
result_manager.add_algorithm("count", lambda input_array: count_sort(input_array, max_value))
#result_manager.add_algorithm("random_quick", random_quick_sort)
#result_manager.add_algorithm("heap", heap_sort_low)
result_manager.run_test(serials=10, array_generator=RandomArrayGenerator(population_size=max_value, sample_size=max_value // 2))


# for i in range(20):
#     sample = random.sample(range(10000), 9000)
#     sorted_results = calculateRunTime(sorted, sample)
#     sorted_times.append(sorted_results[0])

#     #merge_results = calculateRunTime(merge_sort, sample)
#     #insertion_results = calculateRunTime(insertion_sort, sample)
#     heap_results = calculateRunTime(heap_sort, sample)
#     quick_results = calculateRunTime(quick_sort, sample)

#     # if merge_results[1] != sorted_results[1]:
#     #     raise Exception("Merge error:", merge_results[1])
#     # if insertion_results[1] != sorted_results[1]:
#     #     raise Exception("Insertion error:", insertion_results[1])
#     if heap_results[1] != sorted_results[1]:
#         raise Exception("Heap error:", heap_results[1])
#     if quick_results[1] != sorted_results[1]:
#         raise Exception("Quick error:", quick_results[1])

#     # merge_times.append(merge_results[0])
#     # insertion_times.append(insertion_results[0])
#     heap_times.append(heap_results[0])
#     quick_times.append(quick_results[0])


# # print("merge:", sum(merge_times) / len(merge_times))
# #print("insert:", sum(insertion_times) / len(insertion_times))
# print("sorted:", sum(sorted_times) / len(sorted_times))
# print("heap:", sum(heap_times) / len(heap_times))
# print("quick:", sum(quick_times) / len(quick_times))
