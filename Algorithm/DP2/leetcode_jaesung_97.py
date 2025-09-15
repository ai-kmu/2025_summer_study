class Solution:
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False

        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i == len(s1) and j == len(s2):
                cache[(i, j)] = True
                return True
            r1, r2 = False, False
            if i < len(s1) and s1[i] == s3[i + j]:
                r1 = dfs(i + 1, j)
            if not r1 and j < len(s2) and s2[j] == s3[i + j]:
                r2 = dfs(i, j + 1)
            cache[(i, j)] = r1 or r2
            return cache[(i, j)]

        return dfs(0, 0)
