import random
from datetime import datetime

from sorting_lists import selection_sort, insertion_sort, bubble_sort, merge_sort, merge_sorted_lists


def time_it(func,args):
    start = datetime.now()
    func(args)
    return datetime.now() - start


def main():
    ulist = []
    for i in range(0,10000):
        ulist.append(random.randint(1,100000))

    ulist_ss = ulist
    ulist_is = ulist
    ulist_bs = ulist
    ulist_ms = ulist

    time_selection_sort = time_it(selection_sort,ulist_ss)
    time_insertion_sort = time_it(insertion_sort,ulist_is)
    time_bubble_sort = time_it(bubble_sort,ulist_bs)
    time_merge_sort = time_it(merge_sort,ulist_ms)

    print(f"Sorting of {len(ulist)} items -- ")
    print(f"Selection Sort runtime: {time_selection_sort}")
    print(f"Insertion Sort runtime: {time_insertion_sort}")
    print(f"Bubble Sort runtime: {time_bubble_sort}")
    print(f"Merge Sort runtime: {time_merge_sort}")


if __name__ == "__main__":
    main()

#
#   We predict that the Merge Sort will be the fastest sorting algorithm.
#   This is because the expected runtime is on the order of nlog(n) compared
#   to the others, which are expected to run in n**2 time.
#

#
#   Sorting of 10000 items -- Run 1
#   Selection Sort runtime: 0:00:04.205921
#   Insertion Sort runtime: 0:00:13.556395
#   Bubble Sort runtime: 0:00:05.728560
#   Merge Sort runtime: 0:00:00.042089
#

#
#   Sorting of 10000 items -- Run 2
#   Selection Sort runtime: 0:00:04.231275
#   Insertion Sort runtime: 0:00:13.720965
#   Bubble Sort runtime: 0:00:06.650933
#   Merge Sort runtime: 0:00:00.045694
#

#
#   Sorting of 10000 items -- Run 3
#   Selection Sort runtime: 0:00:04.231275
#   Insertion Sort runtime: 0:00:13.720965
#   Bubble Sort runtime: 0:00:06.650933
#   Merge Sort runtime: 0:00:00.045694
#

#
#   As expected the Merge Sort algorithm is noticeable faster than
#   the other sorting algorithms. On average the Merge Sort is
#   100 times faster than the next fastest algorithm, Selection Sort.
#