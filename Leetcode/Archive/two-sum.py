class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        """
        INITIAL THOUGHTS
        # to list out all combinations of nums is too much. 10_000 C 2 = 49_995_000
        allPossibleSums = []
        for j in range(len(nums)):
            allPossibleSums[]
        for i in range(1, len(nums)):
            for j in range(len(nums)):
                allPossibleSums[i*j] = nums[i] + nums[j]
        
        # so if [1,2,3,4,5]
        # aPS[0] = 1, [1] = 2, [2] = 3, [3] = 4, [4] = 5
        # [5] = 2, [6] = 4, [7] = 6, [8] = 8, [9] = 10
        """
        
        """
        METHOD 1: BRUTE-FORCE
        for i in range(len(nums)):
            remainder = target - nums[i]
            for j in range(len(nums)):
                if remainder == nums[j] and i != j:
                    return [i,j]
        """
        
        # METHOD 2: Dictionary -- use more Storage space to reduce Time Complexity from O(n^2) to O(n)
        # 4000ms solution >> 40ms solution!
        d = {}
        for i,n in enumerate(nums):
            m = target - n
            if m in d:
                return d[m], i
            else:
                d[n] = i
