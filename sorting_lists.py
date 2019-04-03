#
#   Sorting list functions
#

def insertion_sort(ulist):
    """
    """
    pass


def bubble_sort(ulist):
    """
    """
    pass

#
#   Selection Sort
#
#   Select sort runs in n**2 time because the
#   algorithm searchs for the largest item in 
#   the list, n number of times. This is a nested
#   for loop.

def selection_sort(ulist):
    """
    Selection-Sort: A function used to sort a list by 
    initializing the largest number in the first slot 
    until it works its way down the entire list.
    
    Run time: My prediction for the Big-O runtime is O(n^2) 
    because of the for-loop and nested for-loop that calculates "n."
    """
    for slot in range(len(ulist)-1,0,-1):
        posOfMax = 0
        for location in range(1,slot+1):
            if ulist[location]> ulist[posOfMax]:
                posOfMax = location

        sort = ulist[slot]
        ulist[slot] = ulist[posOfMax]
        ulist[posOfMax] = sort
    return ulist


def merge_sort(ulist):
    """
    """
    pass
