#
#   Sorting list functions
#

def insertion_sort(ulist):
    """
    """
    pass

#
#   Bubble Sort
#
#   Bubble sort runs in n**2 time. This is because
#   for an item in the index, the item may have to be
#   compared to every othe item in the list. This process
#   then has to happen for each item in the list. This is
#   a nested for loop.
#   

def bubble_sort(ulist):
    """
    Returns sorted list using bubble sort method
    runs at O(n^2)
    """
    for passnum in range(len(ulist)-1,0,-1): #gives a value of position
        print(ulist)
        for i in range(passnum):#it searches for the position equal to i
            if ulist[i]>ulist[i+1]: #if the value of position i is larger than
                temp = ulist[i]
                ulist[i] = ulist[i+1]
                ulist[i+1] = temp
    return ulist
    

def selection_sort(ulist):
    """
    """
    pass


def merge_sort(ulist):
    """
    """
    pass
