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

#A Function to merge the left and right side of the list
#Run Time for my function should be O(nlogn)
def Edgar_Merge_Lists(l, r, list1):
  i = 0
  j = 0
  k = 0
 
  while (i<len(l) and j<len(r)):
    if(l[i]<r[j]):
      list1[k] = l[i]
      i = i+1
    else:
      list1[k] = r[j]
      j = j+1
 
    k = k+1
  
  while(i<len(l)):
    list1[k] = l[i]
    i = i+1
    k = k+1
  
  while(j<len(r)):
    list1[k] = r[j]
    j = j+1
    k = k+1
 
#function for dividing and calling merge function
def Edgar_Merge_Sort(list1):
  n = len(list1)
  if(n<2):
    return
 
  mid = n//2
  l = []
  r = []
  
  for i in range(mid):
    number = list1[i]
    l.append(number)  
   
  for i in range(mid,n):
    number = list1[i]
    r.append(number)
 
  Edgar_Merge_Sort(l)
  Edgar_Merge_Sort(r)
 
  Edgar_Merge_Lists(l,r,list1)

#array to be sorted
list1 = [99,21,19,22,28,11,14,18]
#calling mergesort
Edgar_Merge_Sort(list1)
for i in list1:
  print (i, end = " ")

def merge_sort(ulist):#Devin
    #print("unsorted list")
    #print(ulist)
    if len(ulist)>1:
        mid = len(ulist)//2
        half1 = ulist[:mid]
        half2 = ulist[mid:]
        merge_sort(half1)
        merge_sort(half2)
        i = 0
        j = 0
        k = 0

        while i< len (half1) and j < len(half2):
            if half1[i] < half2[j]:
                ulist[k]=half1[i]
                i = i+1
            else:
                ulist[k] = half2[j]
                j = j+1
            k = k+1

        while i < len(half1):
            ulist[k] = half1[i]
            i = i+1
            k = k+1
        while j < len(half2):
            ulist[k] = half2[j]
            j = j+1
            k = k+1


