#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    # TODO: Create list of counts with a slot for each number in input range
    # TODO: Loop over given numbers and increment each number's count
    # TODO: Loop over counts and append that many numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list

    buckets = []
    for i in range(len(numbers)):
        buckets.append([])

    for num in numbers:
        bucketIndex = num * len(numbers) // (100 + 1)
        buckets[bucketIndex].append(num)

    for i in range(len(buckets)):
        # USE SORTING ALGORITHM FROM RECURSIVE SORTING FILE
        buckets[i] = sorted(buckets[i])

    k = 0
    for i in range(len(numbers)):
        for j in range(len(buckets[i])):
            numbers[k] = buckets[i][j]
            k += 1
    
    return numbers

    # sortedArray = []
    # for bucket in buckets:
    #     for item in bucket:
    #         sortedArray.append(item)
