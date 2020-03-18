# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    # For each element in the array, 
    for i in range(0, len(arr) - 1):
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        # Grab it and compare it to the next
        for j in range(i + 1, len(arr)):
            print("SELECTION", arr)
            #  Grab it and compare it 
            # if next value is lesser, grab that value, switch with the original and restart the process there
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]    
        # TO-DO: swap
        

    return arr

# print("SELECTION", selection_sort([7,3,8,1,9,6]))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(len(arr)):
        # For each element in the array
        for j in range(0, len(arr) - 1):
            print("BUBBLE", arr)
            # Grab it and compare it to the next, checking to see if the original is of greater value
            if arr[j] > arr[j+1]:
                # If the original is of greater value, push it towards the end of the array and check the next one again
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

# print("BUBBLE", bubble_sort([7,3,8,1,9,6]))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr