from collections import Counter
class Solution(object):
    def topKFrequent(self,nums, k):
        count = Counter(nums)
        sorted_elements = sorted(count.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sorted_elements[:k]]
        