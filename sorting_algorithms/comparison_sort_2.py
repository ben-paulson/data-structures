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
        count += heapify(int_list, n, i)
        #count += 2  # heapify makes 2 comparisons
    # sort list
    for i in range(n - 1, 0, -1):  # O(N)
        int_list[i], int_list[0] = int_list[0], int_list[i]
        count += heapify(int_list, i, 0)
        #count += 2  # heapify makes 2 comparisons
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
