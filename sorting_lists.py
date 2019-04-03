#
#   Sorting list functions
#


#
#   Insertion Sort
#
#   Insertion sort runs in n**2 time. This is because for each item
#   in the unsorted list, the algorithm iterates through each
#   item in the sorted list. This is a nested loop.
#

def insertion_sort(ulist):
    """
    Returns sorted numerical list using an insertion sort algorithm
    """
    length = len(ulist)
    sorted_list = []
    sorted_list.insert(0,ulist[0])
    for item in ulist[1:]:
        index = 0
        index_found = False
        if item < sorted_list[index]:
            sorted_list.insert(index,item)
            index_found = True
        while not index_found:
            if index == len(sorted_list)-1:
                sorted_list.append(item)
                index_found = True
            elif item > sorted_list[index] and item < sorted_list[index+1]:
                sorted_list.insert(index+1,item)
                index_found = True
            else:
                index += 1
    return sorted_list


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


#
#   Merge Sort
#   
#   Merge sort runs in nlog(n) time. This is because recursively
#   splitting the unsorted list into two takes log(n) time since
#   the list is split in half each iteration. Merging the lists
#   then runs in linear time, for a combined run time on the order
#   of nlog(n).
#

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
    index_list1 = 0
    index_list2 = 0
    items_left = True
    while items_left:
        if index_list1 >= len(list1):
            combined_list = combined_list + list2[index_list2:]
            items_left = False
        elif index_list2 >= len(list2):
            combined_list = combined_list + list1[index_list1:]
            items_left = False
        elif list2[index_list2] <= list1[index_list1]:
            combined_list.append(list2[index_list2])
            index_list2 += 1
        elif list1[index_list1] <= list2[index_list2]:
            combined_list.append(list1[index_list1])
            index_list1 += 1

    return combined_list
