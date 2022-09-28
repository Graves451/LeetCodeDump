class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashset = {}
        for x in range(len(nums)):
            diff = target - nums[x]
            if diff in hashset:
                return [hashset[diff],x]
            hashset[nums[x]] = x