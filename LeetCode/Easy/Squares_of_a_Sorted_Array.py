class Solution(object):
    def sortedSquares(self, nums):
        array1 = []
        for i in range(len(nums)):
            array1.append(nums[i]**2)
        array1.sort()
        return array1