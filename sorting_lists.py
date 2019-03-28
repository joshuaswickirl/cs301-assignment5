#
#   Sorting list functions
#

def insertion_sort(ulist):
    """
    """
    pass


def bubble_sort(ulist):
    """
    returns sorted list using bubble sort method
    """
    for passnum in range(len(ulist)-1,0,-1): #gives a value of position
        for i in range(passnum):#it searches for the position equal to i
            if ulist[i]>ulist[i+1]: #if the value of position i is larger than
                temp = ulist[i]
                ulist[i] = ulist[i+1]
                ulist[i+1] = temp


def selection_sort(ulist):
    """
    """
    pass


def merge_sort(ulist):
    """
    """
    pass
