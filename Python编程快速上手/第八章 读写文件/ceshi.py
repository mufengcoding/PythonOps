class Solution:
    def twoSum(self, nums, target: int):
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]
