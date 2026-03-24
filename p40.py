def two_sum(nums, target):
    seen = {}  # stores {value: index}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

# Test
print(two_sum([2, 7, 11, 15], 9))   # [0, 1]  → 2 + 7 = 9
print(two_sum([3, 2, 4], 6))        # [1, 2]  → 2 + 4 = 6
print(two_sum([1, 5, 3, 8], 11))    # [1, 3]  → 5 + 8 = 13... wait: [2, 3] → 3+8=11