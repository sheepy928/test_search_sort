import random
import time
from matplotlib import pyplot as plt

# generate a list of random integers
def generate_list(size, max_num=1e6):
    l = []
    for _ in range(size):
        l.append(random.randint(0, max_num))
    return l

# bubble sort
def bubble_sort(l):
    n = len(l)
    for i in range(n):
        for j in range(0, n - i - 1):
            if l[j] > l[j + 1] :
                l[j], l[j + 1] = l[j + 1], l[j]
# insertion sort
def insertion_sort(l):
    for i in range(1, len(l)):
        key = l[i]
        j = i - 1
        while j >= 0 and key < l[j] :
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key

# run the sort algorithms
def sort(l, method):
    if method == 'bubble':
        return bubble_sort(l)
    elif method == 'insertion':
        return insertion_sort(l)
    else:
        return None

# time the process
def time_process(l, method):
    start = time.perf_counter() # use time.per_counter() for better precision than time.time()
    sort(l, method)
    end = time.perf_counter()
    return end - start

def run_test(num, cycle = 10):
    

    result = {"reverse_bubble": 0,
                "reverse_insertion": 0,
                "sorted_bubble": 0,
                "sorted_insertion": 0,
                "unsorted_bubble": 0,
                "unsorted_insertion": 0}

    for _ in range(cycle):
        unsorted_list = generate_list(num) # average case
        reverse_list = sorted(unsorted_list, reverse=True) # worst case
        sorted_list = sorted(unsorted_list) # best case


        # test1: running bubble sort on a reversely sorted list
        result["reverse_bubble"] += time_process(reverse_list, 'bubble')
        # test2: running insertion sort on a reversely sorted list
        result["reverse_insertion"] += time_process(reverse_list, 'insertion')

        # test3: running bubble sort on a sorted list
        result["sorted_bubble"] += time_process(sorted_list, 'bubble')

        # test4: running insertion sort on a sorted list
        result["sorted_insertion"] += time_process(sorted_list, 'insertion')

        # test5: running bubble sort on an unsorted list
        result["unsorted_bubble"] += time_process(unsorted_list, 'bubble')

        # test6: running insertion sort on an unsorted list
        result["unsorted_insertion"] += time_process(unsorted_list, 'insertion')

    return result

# plot the result
def plot_result(results):
    plt.figure(figsize=(10, 7))
    
    plt.title("Time Complexity of Sorting Algorithms")
    plt.xlabel("Size of List")
    plt.ylabel("Time (s)")
    plt.subplot(1, 2, 1)
    plt.plot(size, [x['reverse_bubble'] for x in results], label="reverse_bubble") #
    plt.plot(size, [x['sorted_bubble'] for x in results], label="sorted_bubble") #
    plt.plot(size, [x['unsorted_bubble'] for x in results], label="unsorted_bubble") #
    plt.xlabel("Size of List")
    plt.ylabel("Time (s)")
    plt.title("Bubble Sort")
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(size, [x['reverse_insertion'] for x in results], label="reverse_insertion")
    plt.plot(size, [x['sorted_insertion'] for x in results], label="sorted_insertion")
    plt.plot(size, [x['unsorted_insertion'] for x in results], label="unsorted_insertion")
    plt.xlabel("Size of List")
    plt.ylabel("Time (s)")
    plt.title("Insertion Sort")
    plt.legend()

    plt.suptitle("Time Usage of Sorting Algorithms")
    plt.show()

if __name__ == '__main__':
    size = [500, 1000, 1500, 2000, 2500, 3000]
    results = []
    for i in size:
        results.append(run_test(i))

    plot_result(results)

    
