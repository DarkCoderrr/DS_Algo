def max_sum_subarray_distinct(nums):
    num_index = {}  # Stores the last index of each number
    left = 0        # Left pointer of the sliding window
    max_sum = 0     # Stores the maximum sum found
    current_sum = 0 # Sum of the current window

    for right in range(len(nums)):
        # If the number is already in the window, move the left pointer
        if nums[right] in num_index and num_index[nums[right]] >= left:
            # Remove elements from the sum until the duplicate is removed
            while left <= num_index[nums[right]]:
                current_sum -= nums[left]
                left += 1
        
        # Add the current number to the window
        num_index[nums[right]] = right
        current_sum += nums[right]

        # Update max_sum if the current sum is greater
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example Usage:
nums = [4, 2, 4, 5, 6]
print(max_sum_subarray_distinct(nums)) 
