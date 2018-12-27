class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        
        for i in range(0, n, 1):
            a = nums[i]
            for j in range(i+1, n, 1):
                b = nums[j]
                if a+b == target:
                    result = [i, j]
                    return result
                else:
                    continue
        
