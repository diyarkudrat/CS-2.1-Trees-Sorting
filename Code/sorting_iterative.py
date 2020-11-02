#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: O(n) Why and under what conditions? because you're iterating through each item in array that has a length of n
    TODO: Memory usage: O(1) Why and under what conditions? because we're not storing any additional space. We're just checking the values in the array with each other. """

    for i in range(1, len(items)):
        if items[i] < items[i - 1]:
            return False
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: O(n^2) Why and under what conditions? because you're looping through the array that has a length of n, n amount of times 
    TODO: Memory usage: O(1) Why and under what conditions? because we're not storing any additional space. All we're doing is comparing and swapping which takes constant space"""

    n = 0
    while n < len(items):
        isSwap = False
        for i in range(1, len(items)):
            if items[i] < items[i - 1]:
                items[i], items[i - 1] = items[i - 1], items[i]
                isSwap = True
        if isSwap == False:
            return items
        else:
            n += 1


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: O(n^2) Why and under what conditions? because you're looping through the each item in array n amount of times where n = length of array.
    TODO: Memory usage: O(1) Why and under what conditions? because we're not storing any additional space in this algorithm. We are keeping track of the sorted and 
    unsorted subarrys with pointers."""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item

    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if items[j] < items[min_index]:
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: O(n^2) Why and under what conditions? because we're iterating through every item in the unsorted portion of array including iterating through the sorted portion of array, making the time complexity quadratic
    TODO: Memory usage: O(1) Why and under what conditions? because we're not storing any additional space in this algorithm. We are keeping track of the sorted and 
    unsorted subarrys with pointers."""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items

    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j] < items[j - 1]:
            items[j], items[j - 1] = items[j - 1], items[j]
            j -= 1
        
