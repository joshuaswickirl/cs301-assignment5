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


def selection_sort(ulist):
    for slot in range(len(ulist)-1,0,-1):
        posOfMax = 0
        for location in range(1,slot+1):
            if ulist[location] > ulist[posOfMAx]:
                posOfMax = location
                
    sort = ulist[slot]
    ulist[slot] = ulist[posOfMax]
    ulist[posOfMax] = sort

ulist = [13, 3, 64, 12, 34, 27, 59, 84, 68, 37, 76, 16, 21, 42, 39]
selection_sort(ulist)
print(ulist)
   
    pass


def merge_sort(ulist):
    """
    """
    pass
