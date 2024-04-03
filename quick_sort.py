def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

def replace_elements(sorted_arr, target, replacement):
    for i in range(len(sorted_arr)):
        if sorted_arr[i] == target:
            sorted_arr[i] = replacement
    return sorted_arr

def main():
    # Step 1: Input array of integers
    input_str = input("Enter the array of integers separated by spaces: ")
    arr = list(map(int, input_str.split()))

    # Step 2: Sorting using quick sort algorithm
    sorted_arr = quick_sort(arr[:])

    # Step 3: Display sorted array
    print("Sorted Array:", sorted_arr)

    # Step 4: Searching for target element
    target = int(input("Enter the target element to replace: "))

    if target in sorted_arr:
        # Step 5: Prompt user for replacement element
        replacement = int(input("Enter the replacement element: "))
        # Step 6: Replace target element with replacement
        modified_arr = replace_elements(sorted_arr, target, replacement)
        print("Modified Array:", modified_arr)
    else:
        print("Target element not found in the array.")

if __name__ == "__main__":
    main()