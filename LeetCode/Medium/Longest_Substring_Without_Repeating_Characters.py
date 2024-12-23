# Optimal Approach 1

class Solution(object):
    def lengthOfLongestSubstring(self, str):
        if len(str) == 0:
            return 0
        maxans = float("-inf")
        setx = set()
        l = 0
        for r in range(len(str)):
            if str[r] in setx:
                while l < r and str[r] in setx:
                    setx.remove(str[l])
                    l += 1
            setx.add(str[r])
            maxans = max(maxans, r - l + 1)
        return maxans
        

# Optimal Approach 2

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        mpp = [-1] * 256
        left = 0
        right = 0
        n = len(s)
        length = 0
        while right < n:
            if mpp[ord(s[right])] != -1:
                left = max(mpp[ord(s[right])] + 1, left)
            mpp[ord(s[right])] = right
            length = max(length, right - left + 1)
            right += 1
        return length
        