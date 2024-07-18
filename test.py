def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def iterative_quicksort(arr):
    stack = []

    # Initialize stack with the first pair of indices
    stack.append((0, len(arr) - 1))
    

    # Process the stack until it is empty
    while stack:
        # Pop the top pair of indices
        # print(stack)
        print(arr)
        low, high = stack.pop()
        

        if low < high:
            print("hoer")
            # Partition the array and get the pivot index
            pivot_index = partition(arr, low, high)

            # Push the subarray indices onto the stack
            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))

# Example usage
arr = [3, 6, 8, 10, 1, 2, 1]
iterative_quicksort(arr)
print(arr)  # Outputs: [1, 1, 2, 3, 6, 8, 10]