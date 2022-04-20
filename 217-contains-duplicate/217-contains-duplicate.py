class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        unique_values = set(nums)
        return not len(unique_values) == len(nums)
        