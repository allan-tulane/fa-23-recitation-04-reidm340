# CMPS 2200 Reciation 5
## Answers

**Name:**_________________________


Place all written answers from `recitation-05.md` here for easier grading.







- **1b.**

Randomized List:

|     n |   qsort-fixed-pivot |   qsort-random-pivot |   ssort |   timsort |
|-------|---------------------|----------------------|---------|-----------|
|    10 |               0.008 |                0.010 |   0.007 |     0.001 |
|    50 |               0.041 |                0.051 |   0.047 |     0.001 |
|   100 |               0.096 |                0.109 |   0.155 |     0.001 |
|   200 |               0.191 |                0.242 |   0.556 |     0.002 |
|   500 |               0.506 |                0.596 |   2.878 |     0.003 |
|  1000 |               1.058 |                1.213 |  10.408 |     0.007 |
|  2000 |               1.932 |                2.334 |  34.874 |     0.012 |
|  5000 |               4.636 |                5.447 | 220.283 |     0.024 |
|  7500 |               7.142 |                8.450 | 503.848 |     0.033 |
| 10000 |               9.962 |               11.366 | 909.671 |     0.047 |

Sorted List:

|     n |   qsort-fixed-pivot |   qsort-random-pivot |   ssort |   timsort |
|-------|---------------------|----------------------|---------|-----------|
|    10 |               0.011 |                0.013 |   0.006 |     0.001 |
|    50 |               0.119 |                0.047 |   0.036 |     0.001 |
|   100 |               0.389 |                0.101 |   0.117 |     0.001 |
|   200 |               1.572 |                0.211 |   0.416 |     0.002 |
|   500 |               8.706 |                0.537 |   2.102 |     0.003 |
|  1000 |              27.776 |                0.919 |   6.994 |     0.005 |
|  2000 |             106.764 |                1.906 |  27.404 |     0.012 |
|  5000 |             680.421 |                4.948 | 178.568 |     0.023 |
|  7500 |            1534.568 |                7.978 | 400.476 |     0.032 |
| 10000 |            2837.032 |               10.694 | 756.311 |     0.044 |

Quicksort: $W(n) = O(n^2)$

           W(n)= Θ(nlogn)

Selection Sort: $W(n) = O(n^2)$

                W(n)= Θ(n^2)

By changing the list from random to sorted, fixed pivot (pivot = a[0]) quicksort becomes significantly less efficient. In contrast, there is not much of a change in random pivot quicksort or timsort and an increase in efficiency in selection sort.

The work of quicksort and selection sort explain these differences we see between random pivot quicksort and selection sort. Since selection sort grows exponentially, it makes sense that, even though it starts off faster at small n values, it ends up being far less efficient at larger ones.

Fixed pivot is likely less efficient on the sorted version since it isn't really even dividing up the work. If the pivot is the first, smallest input into the list, then the left-hand list will be empty on every recursive call. As a result, the loop has to run n times. However, this version runs fine when the list is randomized. This is because the pivot isn't necessarily the smallest input in the list for each recursive call.

- **1c.**

Refer to the same graphs as above, timsort included in rightmost column.

Timsort is much faster than all other methods. This holds at smaller n values, larger n values, randomized lists, and sorted lists.