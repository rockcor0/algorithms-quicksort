def quicksort(myArray):
    # Base case
    if len(myArray) < 2:
        return myArray
    else:
        pivot = myArray[0]  # <- Recursive case
        # Array with elements less than pivot
        less = [i for i in myArray[1:] if i <= pivot]
        # Array with elements higher than pivot
        higher = [i for i in myArray[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(higher)


print(quicksort([10, 5, 2, 3, 4, 5, 7, 1, 6, 0, 4, 9, 8]))
