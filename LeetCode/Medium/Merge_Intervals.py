# Brute Force Approach

class Solution(object):
    def merge(self, intervals):
        n = len(intervals)
        intervals.sort()
        ans = []
        for i in range(n):
            start,end = intervals[i][0],intervals[i][1]
            if ans and end <= ans[-1][1]:
                continue
            for j in range(i+1,n):
                if intervals[j][0] <= end:
                    end = max(end,intervals[j][1])
                else:
                    break
            ans.append([start,end])
        return ans
        
# Optimal Approach

class Solution(object):
    def merge(self, intervals):
        n = len(intervals)
        intervals.sort()
        ans = []
        for i in range(n):
            if not ans or intervals[i][0] > ans[-1][1]:
                ans.append(intervals[i])
            else:
                ans[-1][1] = max(ans[-1][1],intervals[i][1])
        return ans
        