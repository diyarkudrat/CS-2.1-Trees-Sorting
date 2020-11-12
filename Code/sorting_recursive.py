#!python


def merge(array, leftIdx, rightIdx, middle):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: O(n + m) Why and under what conditions? Looping through every value in an array with length of n and another array with length of m
    TODO: Memory usage: O(n) Why and under what conditions? we're storing n amount of values in a sorted list which takes up space
    """ 
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list
    leftHalf = array[leftIdx:middle + 1]
    rightHalf = array[middle + 1: rightIdx + 1]

    i = 0
    j = 0
    sortedArrayIdx = leftIdx

    while i < len(leftHalf) and j < len(rightHalf):
        if leftHalf[i] <= rightHalf[j]:
            array[sortedArrayIdx] = leftHalf[i]
            i += 1
        else:
            array[sortedArrayIdx] = rightHalf[j]
            j += 1

        sortedArrayIdx += 1

    while i < len(leftHalf):
        array[sortedArrayIdx] = leftHalf[i]
        i += 1
        sortedArrayIdx += 1

    while j < len(rightHalf):
        array[sortedArrayIdx] = rightHalf[j]
        j += 1
        sortedArrayIdx += 1



def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half using any other sorting algorithm
    # TODO: Merge sorted halves into one list in sorted order
    
    




def merge_sort(array, leftIdx, rightIdx):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order
    if leftIdx >= rightIdx:
        return
    
    middle = (leftIdx + rightIdx) // 2
    mergeSort(array, leftIdx, middle)
    mergeSort(array, middle + 1, rightIdx)
    merge(array, leftIdx, rightIdx, middle)


def partition(items, start, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (Pivot will be the first value of array) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p

    pivot = items[start]
    low = start + 1

    while True:
        while low <= high and items[low] <= pivot:
            low += 1

        while low <= high and items[high] >= pivot:
            high -= 1

        if low <= high:
            items[low], items[high] = items[high], items[low]
        else:
            break
            
    items[start], items[high] = items[high], items[start]

    return high


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort
    if low >= high:
        return

    p = partition(items, low, high)
    quick_sort(items, low, p - 1)
    quick_sort(items, p + 1, high)
