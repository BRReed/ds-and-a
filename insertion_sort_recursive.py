


def insertion_sort(unsorted_a, data_index=1, compare_index=0):
    """Sorts an array, not dependent on data type

    Args:
        unsorted_a (Array): an array
        data_index (Int): index in array, do not pass var
        compare_index (Int): index in array to compare against data_index

    Returns:
        (Array): sorted unsorted_a
    """
    if data_index > len(unsorted_a) - 1:
        return unsorted_a
    data = get_data(unsorted_a, data_index)
    compare = get_data(unsorted_a, compare_index)
    if data >= compare:
        unsorted_a = swap(unsorted_a, data_index, compare_index+1)
        insertion_sort(unsorted_a, data_index+1, data_index)
    if data < compare and compare_index == 0:
        unsorted_a = swap(unsorted_a, data_index, compare_index)
        insertion_sort(unsorted_a, data_index+1, data_index)
    elif data < compare:
        insertion_sort(unsorted_a, data_index, compare_index-1)
    else:
        return unsorted_a

def get_data(array, index):
    """takes an array and index and returns the data at that index

    Args:
        array (Array): an array of any type
        index (Int): in integer corresponding with the index of data you want

    Returns:
        [Misc]: what is at the index of the passed array
    """
    return array[index]

def swap(array, data_index, compare_index):
    """takes an array, swaps data from data_index down to compare_index and 
       moves all data inbetween one to the right

    Args:
        array (Array): [description]
        data_index (Int): index for data to be movedneeds to be > than 
                          compare_index
        compare_index (Int): stopping point for data at data_index
                             must be < than data_index

    Returns:
        Array: modified array
    """
    i = data_index
    data = get_data(array, data_index)
    while i != compare_index:
        move_to = i
        i -= 1
        move_data = get_data(array, i)
        array[move_to] = move_data
    array[compare_index] = data
    return array




print(insertion_sort([5, 6, 4, 6, 2, 1, 7, 4]))
print(insertion_sort([9, 19, 85, 99, 32, 0, 33, 123, 34, 33, 12]))

