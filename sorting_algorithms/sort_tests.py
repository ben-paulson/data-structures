"""Sorting algorithm tests and data collection.
Authors: Nick Gazdak, Benjamin Paulson, Nickzad Bayati
"""

import logging
import random
import time
import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import make_interp_spline
from comparison_sort import *


def make_plot(x, y, name, color, sorted=False):
    """Adds the plot data to both the overall plot (of all algorithms)
    as well as a new plot to contain only the data from the last algorithm.
    Arguments:
        x (numpy array): Test array sizes, plotted on x-axis
        y (numpy array): Number of comparisons, plotted on y-axis
        name (str): Name of the sorting algorithm being plotted
        color (str): Color of the data points (next automatic in queue)
        sorted (bool): Optional argument to change labeling to indicate that
                       the data plot is from a test with a pre-sorted list
    """
    srt = ""
    filename = f'{name}.png'
    # Make smooth lines
    x_smooth = np.linspace(x.min(), x.max(), 300)
    spline = make_interp_spline(x, y)
    y_smooth = spline(x_smooth)
    # Plot results of each algorithm in a single plot all together
    plt.figure(1)
    if sorted:
        plt.figure(2)
        srt = " (Sorted)"
        filename = f'{name}_sorted.png'
    plt.plot(x, y, 'o', color=color)
    plt.plot(x_smooth, y_smooth, '-', label=name, color=color)
    # Switch to a new plot for this algorithm alone
    plt.figure()
    plt.plot(x, y, 'o', color=color)
    plt.plot(x_smooth, y_smooth, '-', color=color)
    plt.title(name + srt)
    plt.ylabel('Number of Comparisons')
    plt.xlabel('Size of list')
    plt.grid(True)
    # Save the data as a plot by itself
    plt.savefig(filename, bbox_inches='tight')


def configure_plot_all(sorted=False):
    """Configures settings for the plot of all algorithms on the same graph
    and saves the plot to a file
    Arguments:
        sorted (bool): Optional argument to configure the plot of all
                       tests that were performed with pre-sorted lists
    """
    file_output = "all.png"
    plt.figure(1)
    plt.title('Comparison of Sorting Algorithms')
    if sorted:
        file_output = "all_sorted.png"
        plt.figure(2)
        plt.title('Comparison of Sorting Algorithms With Pre-Sorted Lists')
    plt.ylabel('Number of Comparisons')
    plt.xlabel('Size of list')
    plt.grid(True)
    plt.legend()
    plt.savefig(file_output, bbox_inches='tight')


def test_algorithm(algorithm, test_sizes, sorted=False):
    """Runs tests of various array sizes on the specified algorithm
    and logs the runtime and number of comparisons to a log file.
    Arguments:
        algorithm (function): The algorithm to run.
        test_sizes (list): The various array sizes to test the algorithm on.
        sorted (bool): Optional argument to test with a pre-sorted list
    Returns:
        list: A list containing the number of comparisons done in each test.
    """
    comparisons = []
    srt = ""
    for items in test_sizes:
        alist = random.sample(range(items * 10), items)
        if sorted:
            timsort_start = time.time()
            alist.sort()
            timsort_time = time.time() - timsort_start
            srt = " SORTED"
            # Log the time it takes for builtin sort() to run
            logging.info(f"Timsort on list with {items} items" +
                         f" finished in {timsort_time} seconds")
        start = time.time()
        num_comparisons = algorithm(alist)
        end = time.time()
        comparisons.append(num_comparisons)
        logging.info(f"{algorithm.__name__} with {items}{srt} items " +
                     f"finished in {end - start} seconds with " +
                     f"{num_comparisons} comparisons.")
    print(f"Finished {algorithm.__name__}{srt}")
    logging.info('') # Separate test entries by a space
    return comparisons


def main():
    # Setup log file
    LOGFILE = 'results.log'
    logging.basicConfig(filename=LOGFILE, level=logging.INFO)
    # Clear log file
    with open(LOGFILE, 'w'):
        pass
    # Functions from comparison_sort.py
    search_algorithms = [quick_sort, heap_sort, merge_sort,
                         selection_sort, insertion_sort, bubble_sort]
    random.seed(1) #in order to generate the same sequence of numbers each time.
    test_sizes = [1000, 2000, 4000, 8000, 16000, 32000, 100000, 500000]
    x_data = np.array(test_sizes)
    # Run the tests
    for color_queue_idx, algorithm in enumerate(search_algorithms):
        # Test algorithm with an unsorted list
        comparisons = test_algorithm(algorithm, test_sizes)
        y_data = np.array(comparisons)
        # Repeat test with a sorted list
        comparisons_srt = test_algorithm(algorithm, test_sizes, sorted=True)
        y_data_srt = np.array(comparisons_srt)
        color = 'C' + str(color_queue_idx)
        # Make a plot for both sorted and unsorted results
        make_plot(x_data, y_data, algorithm.__name__, color)
        make_plot(x_data, y_data_srt, algorithm.__name__, color, sorted=True)
    # Make the plots for all sorted and unsorted algorithms together
    configure_plot_all()
    configure_plot_all(sorted=True)
    logging.info('Done.')


if __name__ == '__main__':
    main()
