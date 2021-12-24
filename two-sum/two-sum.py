class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        target_differences = {}
        for i,j in enumerate(nums):
            difference = target - j
            if difference in target_differences:
                return [target_differences[difference],i]
            
            target_differences[j] = i 