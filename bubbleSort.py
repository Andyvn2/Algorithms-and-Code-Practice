def bubbleSort(items):

    def swap(firstIndex, secondIndex):
        temp = items[firstIndex]
        items[firstIndex] = items[secondIndex]
        items[secondIndex] = temp

    length = len(items)

    for i in range(length):
        j = 0
        stop = length - i
        while j < stop - 1:
            if items[j] > items[j + 1]:
                swap(j, j + 1)
            j += 1
    return items


# For items = [2, 4, 1, 5], the output should be
# bubbleSort(items) = [1, 2, 4, 5].

# Input/Output

# [execution time limit] 4 seconds (py)

# [input] array.integer items

# Guaranteed constraints:
# 1 ≤ items.length ≤ 15,
# -100 ≤ items[i] ≤ 100.

# [output] array.integer

