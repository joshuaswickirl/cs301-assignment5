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
    """
    """
    pass


def merge_sort(ulist):
    """
    Recurisvely splits list into individual items
    then uses merge to join them in order.
    """
    if len(ulist) <= 1:
        return ulist
    else:
        mid = len(ulist) // 2
        list1 = ulist[:mid]
        list2 = ulist[mid:]
        return merge_sorted_lists(merge_sort(list1), merge_sort(list2))


def merge_sorted_lists(list1,list2=[]):
    """
    Returns two sorted lists combined into one
    sorted list.
    """
    combined_list = []
    items_left = True
    while items_left:
        len_list1 = len(list1)
        len_list2 = len(list2)
        if len_list1 == 0 and len_list2 == 0:
            items_left = False
        elif len_list1 == 0 and len_list2 > 0:
            combined_list = combined_list + list2
            items_left = False
        elif len_list2 == 0 and len_list1 > 0:
            combined_list = combined_list + list1
            items_left = False
        elif list1[0] >= list2[0]:
            combined_list.append(list2.pop(0))
        else:
            combined_list.append(list1.pop(0))

    return combined_list