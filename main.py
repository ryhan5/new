def moveZeroes(nums):
    left = 0
    right = 0

    while right < len(nums):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1

    nums[left:] = [0] * (len(nums) - left)

# Example usage:
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]
