import random
import time
from matplotlib import pyplot as plt

# generate a list of random integers
def generate_list(size, max_num=1e6):
    l = []
    for _ in range(size):
        l.append(random.randint(0, max_num))
    return l

# linear search
def linear_search(l, key):
    for i in range(len(l)):
        if l[i] == key:
            return i
    return -1

# iterative binary search of a sorted list
def binary_search(l, key):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if l[mid] == key:
            return mid
        elif l[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# # recursive binary search of a sorted sorted list
# def recursive_binary_search(l, key):
#     if len(l) == 0:
#         return -1
#     else:
#         mid = len(l) // 2
#         if l[mid] == key:
#             return mid
#         elif l[mid] < key:
#             return recursive_binary_search(l[mid+1:], key)
#         else:
#             return recursive_binary_search(l[:mid], key)

# run the search algorithms
def search(list, key, method):
    if method == 'linear':
        return linear_search(list, key)
    elif method == 'binary':
        return binary_search(list, key)
    # elif method == 'recursive':
    #     return recursive_binary_search(list, key)
    else:
        return -1

# randomly choose one number if the list
def choose_key(list):
    return list[random.randint(0, len(list) - 1)]

# test1: running linear search on an unsorted and a sorted list
def run_test1(num, cycle = 50):
    print("Running linear search on an unsorted and a sorted list...")
    time_unsorted = []
    time_sorted = []
    for _ in range(cycle):
        unsorted_list = generate_list(num)
        sorted_list = sorted(unsorted_list)
        key = choose_key(unsorted_list)

        start = time.perf_counter()
        search(unsorted_list, key, 'linear')
        end = time.perf_counter()
        time_unsorted.append(end - start)

        # print("Running linear search on sorted_list1...")
        start = time.perf_counter()
        search(sorted_list, key, 'linear')
        end = time.perf_counter()
        time_sorted.append(end - start)

    print("\tTotal time for linear search on unsorted_list: {}, size: {}, cycle: {}".format(sum(time_unsorted), num, cycle))
    print("\tTotal time for linear search on sorted_list: {}, size: {}, cycle: {}".format(sum(time_sorted), num, cycle))

    return sum(time_unsorted), sum(time_sorted)

# test2: running linear and binary search on a sorted list
def run_test2(num, cycle = 50):
    print("Running linear and binary search on a sorted list...")
    time_linear = []
    time_binary = []
    for _ in range(cycle):
        sorted_list = sorted(generate_list(num))
        key = choose_key(sorted_list)

        start = time.perf_counter()
        search(sorted_list, key, 'linear')
        end = time.perf_counter()
        time_linear.append(end - start)

        # print("Running binary search on sorted_list1...")
        start = time.perf_counter()
        search(sorted_list, key, 'binary')
        end = time.perf_counter()
        time_binary.append(end - start)

    print("\tTotal time for linear search on sorted_list: {}, size: {}, cycle: {}".format(sum(time_linear), num, cycle))
    print("\tTotal time for binary search on sorted_list: {}, size: {}, cycle: {}".format(sum(time_binary), num, cycle))

    return sum(time_linear), sum(time_binary)

def plot_result(test1, test2):
    # plot the results
    plt.figure(figsize=(10, 7))
    plt.subplot(1, 2, 1)
    plt.plot(size, test1["unsorted"], label = "linear search on unsorted list")
    plt.plot(size, test1["sorted"], label = "linear search on sorted list")
    plt.xlabel("Size of list")
    plt.ylabel("Time (s)")
    plt.legend()
    plt.title("linear search on unsorted and sorted list")

    plt.subplot(1, 2, 2)
    plt.plot(size, test2["linear"], label = "linear search on sorted list")
    plt.plot(size, test2["binary"], label = "binary search on sorted list")
    plt.xlabel("Size of list")
    plt.ylabel("Time (s)")
    plt.legend()
    plt.title("linear and binary search on sorted list")

    plt.suptitle("Linear and Binary Search on Sorted and Unsorted Lists")
    plt.show()

# main
if __name__ == '__main__':
    size = [5000, 10000, 15000, 20000, 25000, 30000]
    test1 = {"unsorted": [], "sorted": []}
    test2 = {"linear": [], "binary": []}
    for i in size:
        r1, r2 = run_test1(i)
        print("\n")
        test1["unsorted"].append(r1)
        test1["sorted"].append(r2)
        r3, r4 = run_test2(i)
        print("\n")
        test2["linear"].append(r3)
        test2["binary"].append(r4)
    
    plot_result(test1, test2)
    print(test1)
    print(test2)

