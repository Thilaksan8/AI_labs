def minimumSwaps(arr):
    n = len(arr)
    swaps = 0
    visited = [False] * n
    # Create a sorted version and map original indices
    sorted_arr = sorted([(val, i) for i, val in enumerate(arr)])

    for i in range(n):
        if visited[i] or sorted_arr[i][1] == i:
            continue

        cycle_size = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = sorted_arr[j][1]
            cycle_size += 1

        if cycle_size > 0:
            swaps += cycle_size - 1

    return swaps

result=minimumSwaps([4, 3, 1, 2])
print(result)  