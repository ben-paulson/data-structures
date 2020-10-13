""" Sorting Algorithms
Authors: Nick Gazdak, Benjamin Paulson, Nickzad Bayati
"""
import random, time

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
    print(str(alist) + str(lo) + str(hi))
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

items = 1000
alist = random.sample(range(items * 10), items)
# print(alist)
print(quick_sort(alist), "Comparisons")
# print(alist)
