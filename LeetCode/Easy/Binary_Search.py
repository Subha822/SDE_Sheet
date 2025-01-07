class Solution(object):
    def search(self, nums, target):
        return self.binarySearch(nums, 0, len(nums) - 1, target)
        
    def binarySearch(self, nums, low, high, target):
        if low > high:
            return -1
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            return self.binarySearch(nums, mid + 1, high, target)
        return self.binarySearch(nums, low, mid - 1, target)
