def selectionsort(array):
    for index in range(len(array)):
        min_index = index
        for j in range(index + 1, len(array)):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
        # swapping the elements to sort the arra
        (array[index], array[min_index]) = (array[min_index], array[index])
    return array


