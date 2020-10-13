"""Sorting algorithms.
Authors: Nick Gazdak, Benjamin Paulson, Nickzad Bayati
"""


def selection_sort(alist):
    """Sorts a list using the selection sort algorithm.
    Author: Ben Paulson
    Arguments:
        alist (list): The list to sort
    Returns:
        int: The number of comparisons made during the runtime
    """
    num_comparisons = 0
    sorted_idx = len(alist) - 1
    for i, _ in enumerate(alist):
        largest_idx = 0
        for j in range(sorted_idx):
            num_comparisons += 1
            if alist[j] > alist[largest_idx]:
                largest_idx = j
        temp = alist[largest_idx]
        alist[largest_idx] = alist[sorted_idx]
        alist[sorted_idx] = temp
        sorted_idx -= 1
    return num_comparisons


def merge_sort(alist):
    """Sorts a list using the merge sort algorithm.
    Author: Ben Paulson
    Arguments:
        alist (list): The list to sort
    Returns:
        int: The number of comparisons made during the runtime
    """
    num_comparisons = 0
    mid = len(alist) // 2
    left = alist[:mid]
    right = alist[mid:]
    # Stop dividing list when there is only a
    # single item to avoid recursion error
    if len(alist) != 1:
        num_comparisons += merge_sort(left)
        num_comparisons += merge_sort(right)
    num_comparisons += merge(alist, left, right)
    return num_comparisons


def merge(arr, left, right):
    """Helper function for merge_sort. Merges two arrays into one sorted array
    Author: Ben Paulson
    Arguments:
        arr (list): The merged array
        left (list): The left half of the array that was previously split.
                     Will be merged with right.
        right (list): The right half of the array that was previously split.
                      Will be merged with left.
    Returns:
        int: Number of comparisons made during the merge
    """
    num_comparisons = 0
    i = 0 # Left array index
    j = 0 # Right array index
    merged_idx = 0 # Index of merged lists
    # Take the smallest between the current indexes of left and right
    # and add it to the larger array (alist)
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            arr[merged_idx] = right[j]
            j += 1
        else:
            arr[merged_idx] = left[i]
            i += 1
        merged_idx += 1
        num_comparisons += 1
    # Add whatever is left over when one array finishes before the other
    for num in left[i:]:
        arr[merged_idx] = num
        merged_idx += 1
        num_comparisons += 1
    for num in right[j:]:
        arr[merged_idx] = num
        merged_idx += 1
        num_comparisons += 1
    return num_comparisons


def heapify(int_list, n, index):
    """Function that heapifies a list of integers into a max heap.
    Author: Nickzad Bayati
    Args:
      int_list (list): a list of random integers
      n (int): the number of integers in the list
      index (int): The index of the subtree root
    Returns:
      list: integer list in max heap order
    """
    count = 0
    largest = index  # root is initially the largest
    left = 2 * index + 1  # left child
    right = 2 * index + 2  # right child
    # left vs root comparison
    if left < n and int_list[largest] < int_list[left]:
        largest = left
        count += 1
    # right vs root comparison
    if right < n and int_list[largest] < int_list[right]:
        largest = right
        count += 1
    # if the largest value changed
    if largest != index:
        int_list[index], int_list[largest] = int_list[largest], int_list[index]
        count += heapify(int_list, n, largest)
    return count


def heap_sort(int_list):
    """Function that sorts a list of integers using heap sort.
    Author: Nickzad Bayati
    Args:
      int_list (list): list of random integers
    Returns:
      int: count of the number of comparisons made
    """
    n = len(int_list)
    count = 0
    # organize list into a max heap
    for i in range(n // 2 - 1, -1, -1):  # O(logN)
        count += heapify(int_list, n, i) # Add comparisons from heapify
    # sort list
    for i in range(n - 1, 0, -1):  # O(N)
        int_list[i], int_list[0] = int_list[0], int_list[i]
        count += heapify(int_list, i, 0) # Add comparisons from heapify
    return count


def bubble_sort(int_list):
    """Function that sorts a list of integers using bubble sort.
    Author: Nickzad Bayati
    Args:
      int_list (list): a list of random integers
    Returns:
      int: count of the number of comparisons made
    """
    count = 0
    for i in range(len(int_list)):
        for j in range(len(int_list) - 1 - i):
            if int_list[j] > int_list[j + 1]:
                int_list[j], int_list[j + 1] = int_list[j + 1], int_list[j]
            count += 1
    return count


def insertion_sort(alist):
    """ Insertion sort algorithm, counts comparisons
    Author:
        Nick Gazdak
    Args:
        alist(list): list of integers
    returns:
        (int): the number of comparisons made
    """
    size = len(alist)
    comparisons = 0
    for i in range(1, size):
        j = i
        #comparisons += 1
        while j > 0 and alist[j - 1] > alist[j]:
            alist[j-1], alist[j] = alist[j], alist[j-1]
            j -= 1
            comparisons += 1
    return comparisons


def quick_sort(alist, lo=None, hi=None, count=0):
    """ Quicksort algorithm, counts comparisons
    Author :
        Nick Gazdak
    Args:
        alist(list): list of integers
    returns:
        (int): the number of comparisons made
    """
    if lo is None and hi is None:
        lo = 0
        hi = (len(alist) - 1)
    if lo >= hi:
        return count
    # calculating and moving mid index to front
    mid = (lo + hi) // 2
    val = alist[lo]
    alist[lo] = alist[mid]
    alist[mid] = val
    #Creating left and right pointer
    left = lo + 1
    right = hi
    #print(str(alist) + str(lo) + str(hi))
    while left <= right:
        count += 1
        #move left pointer right until it points to an item
        #whose val is larger than pivot value
        while left <= hi and alist[left] <= alist[lo]:
            if left > right:
                break
            left += 1
        #move right pointer left until it points to an item
        #whose val is less than pivot value
        while right > lo and alist[right] >= alist[lo]:
            if left > right:
                break
            right -= 1
        #Swap left and right indexes until pointers pass
        #print('before swap' + str(alist))
        if left > right:
                break
        val = alist[left]
        alist[left] = alist[right]
        alist[right] = val

    #swap mid index and right back
    val = alist[lo]
    alist[lo] = alist[right]
    alist[right] = val
    #recursive calls on sublists
    count_1 = quick_sort(alist, lo, right - 1, count)
    count_2 = quick_sort(alist, right + 1, hi, count)
    return count_1 + count_2
