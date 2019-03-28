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
   ***
   Selections Sort 
   ***
   for slot in range(len(ulist)-1,0,-1):
       posOfMax = 0
       for location in range(1,slot+1):
           if ulist[location]> ulist[posOfMax]:
                posOfMax = location

       sort = ulist[slot]
       ulist[slot] = ulist[posOfMax]
       ulist[posOfMax] = sort


def merge_sort(ulist):
    """
    """
    pass
