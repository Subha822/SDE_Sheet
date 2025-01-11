class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maximum = 0
        count = 0
        for i in range(len(nums)):
            if nums[i]==0:
                count = 0
            count = count + nums[i]
            maximum = max(maximum,count)
        return maximum