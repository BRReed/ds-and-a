

def insertion_sort(array):
    for i in range(0, len(array)):
        while i != 0:
            if array[i] < array[i-1]:
                array = swap(array, i)
            i -= 1
    return array

def swap(array, i):
    temp = array[i]
    array[i] = array[i-1]
    array[i-1] = temp
    return array



