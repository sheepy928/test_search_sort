import random
import time
from matplotlib import pyplot as plt

# generate a list of random integers
def generate_list(size):
    l = []
    for i in range(size):
        l.append(random.randint(0, size))
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

def run_test(num, cycle = 6):
    unsorted_list = generate_list(num) # average case
    reverse_list = sorted(unsorted_list, reverse=True) # worst case
    sorted_list = sorted(unsorted_list) # best case

    result = {"reverse_bubble": [],
                "reverse_insertion": [],
                "sorted_bubble": [],
                "sorted_insertion": [],
                "unsorted_bubble": [],
                "unsorted_insertion": []}

    for _ in range(cycle):
        # test1: running bubble sort on a reversely sorted list
        result["reverse_bubble"].append(time_process(reverse_list, 'bubble'))

        # test2: running insertion sort on a reversely sorted list
        result["reverse_insertion"].append(time_process(reverse_list, 'insertion'))

        # test3: running bubble sort on a sorted list
        result["sorted_bubble"].append(time_process(sorted_list, 'bubble'))

        # test4: running insertion sort on a sorted list
        result["sorted_insertion"].append(time_process(sorted_list, 'insertion'))

        # test5: running bubble sort on an unsorted list
        result["unsorted_bubble"].append(time_process(unsorted_list, 'bubble'))

        # test6: running insertion sort on an unsorted list
        result["unsorted_insertion"].append(time_process(unsorted_list, 'insertion'))

    return result


if __name__ == '__main__':
    size = [500, 1000, 1500, 2000, 2500, 3000]
    results = []
    for i in size:
        results.append(run_test(i))

    # plot the results
    plt.figure(figsize=(10, 10))
    plt.title("Time Complexity of Sorting Algorithms")
    plt.xlabel("Size of List")
    plt.ylabel("Time (s)")
    plt.plot(size, results[0]["reverse_bubble"], label="reverse_bubble") #
    plt.plot(size, results[0]["reverse_insertion"], label="reverse_insertion")
    plt.plot(size, results[0]["sorted_bubble"], label="sorted_bubble") #
    plt.plot(size, results[0]["sorted_insertion"], label="sorted_insertion")
    plt.plot(size, results[0]["unsorted_bubble"], label="unsorted_bubble") #
    plt.plot(size, results[0]["unsorted_insertion"], label="unsorted_insertion")
    plt.legend()
    plt.show()

    
