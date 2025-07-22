def closestPairSum(arr):
    arr.sort()
    min_diff = float('inf')
    max_abs_sum = 0

    for i in range(len(arr) - 1):
        diff = abs(arr[i] - arr[i+1])
        abs_sum = abs(arr[i]) + abs(arr[i+1])

        if diff < min_diff:
            min_diff = diff
            max_abs_sum = abs_sum
        elif diff == min_diff:
            max_abs_sum = max(max_abs_sum, abs_sum)
    
    return max_abs_sum
result = closestPairSum([1, 3, -2, 5, 4])
print(result)