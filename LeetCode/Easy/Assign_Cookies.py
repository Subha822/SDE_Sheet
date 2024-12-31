class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        n = len(g)
        m = len(s)
        l = 0
        r = 0
        while l < m and r < n:
            if g[r] <= s[l]:
                r = r+1
            l = l+1
        return r