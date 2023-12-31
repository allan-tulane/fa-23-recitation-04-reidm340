import random, time
import tabulate
import sys
sys.setrecursionlimit(100001)

def qsort(a, pivot_fn):
    ## TO DO
    if len(a) <= 1:
        return a
    else:
        pivot = pivot_fn(a)
        left_set = []
        pivot_set = []
        right_set = []
        for value in a:
            if value < pivot:
                left_set.append(value)
            elif value == pivot:
                pivot_set.append(value)
            else:
                right_set.append(value)

        left_sorted = qsort(left_set, pivot_fn)
        right_sorted = qsort(right_set, pivot_fn)

        return left_sorted + pivot_set + right_sorted
    
def ssort(L):
    for i in range(len(L)):
        #print(L)
        m = L.index(min(L[i:]))
        L[i], L[m] = L[m], L[i]
    return L
    
def time_search(sort_fn, mylist):
    """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds. 
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key 

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000
    ###

def qsort_fixed_pivot(unsorted_list):
    qsort(unsorted_list,lambda a: a[0])

def qsort_random_pivot(unsorted_list):
    qsort(unsorted_list, lambda a: random.choice(a))

def compare_sort(sizes=[10, 50, 100, 200, 500, 1000, 2000, 5000, 7500, 10000]):
    """
    Compare the running time of different sorting algorithms.

    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """
    ### TODO - sorting algorithms for comparison
    #tim_sort = sorted(mylist)
    result = []
    for size in sizes:
        # create list in ascending order
        mylist = list(range(size))
        # shuffles list if needed
        random.shuffle(mylist)
        result.append([
            len(mylist),
            time_search(qsort_fixed_pivot, mylist),
            time_search(qsort_random_pivot, mylist),
            time_search(ssort, mylist),
            time_search(sorted, mylist)
        ])
    return result
    ###

def print_results(results):
    """ change as needed for comparisons """
    print(tabulate.tabulate(results,
                            headers=['n', 'qsort-fixed-pivot', 'qsort-random-pivot', 'ssort', 'timsort'],
                            floatfmt=".3f",
                            tablefmt="github"))

def test_print():
   print_results(compare_sort())

random.seed()
test_print()
