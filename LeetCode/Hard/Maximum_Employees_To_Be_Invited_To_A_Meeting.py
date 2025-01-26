class Solution:
    def maximumInvitations(self, favorite):
        n = len(favorite)
        when = [0] * n
        vis = [False] * n
        res = 0
        def func(at, level): 
            if vis[at]:
                return 0
            if when[at] != 0:
                return level - when[at]
            when[at] = level
            length = func(favorite[at], level + 1)
            vis[at] = True
            return length
        for i in range(n):
            res = max(res, func(i, 1))
        g = defaultdict(list)
        for u, v in enumerate(favorite):
            g[v].append(u)
        def func(at, level, exclude): 
            x = level
            for next in g[at]:
                if next != exclude:
                    x = max(x, func(next, level + 1, exclude))
            return x
        return max(res, sum(func(i, 1, favorite[i]) if i == favorite[favorite[i]] else 0 for i in range(n)))