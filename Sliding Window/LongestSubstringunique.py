def longest_unique_substring(s):
    char_index = {}
    left = 0
    max_length = 0
    start_index = 0  # To track the start of the longest substring

    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1  # Move left pointer to avoid repetition

        char_index[s[right]] = right  # Update last seen index of the character

        if right - left + 1 > max_length:
            max_length = right - left + 1
            start_index = left  # Update start index of longest substring

    return s[start_index: start_index + max_length]

# Example Usage:
s = "abcabcbb"
print(longest_unique_substring(s))
