class Solution:
    """
    Problem: 1. Two Sum
    Pattern: Arrays & Hashing (Hash Map)
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        PastNums = {}

        for n in range(len(nums)):
            CompNum = target - nums[n]

            if CompNum in PastNums:
                return [PastNums[CompNum], n]

            PastNums[nums[n]] = n

        return []
