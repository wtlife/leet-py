from typing import List


class Hot100_solution:
    def is_match(self, s: str, p: str) -> bool:
        m = len(s) + 1
        n = len(p) + 1

        dp = [[False for c in range(n)] for r in range(m)]
        dp[0][0] = True
        for i in range(0, len(p)):
            if p[i] == '*' and dp[0][i - 1]:
                dp[0][i + 1] = True

        for i in range(0, len(s)):
            for j in range(0, len(p)):
                if s[i] == p[j] or p[j] == '.':
                    dp[i + 1][j + 1] = dp[i][j]

                if p[j] == '*':
                    if p[j - 1] != s[i] and p[j - 1] != '.':
                        dp[i + 1][j + 1] = dp[i + 1][j - 1]
                    else:
                        dp[i + 1][j + 1] = dp[i + 1][j - 1] or dp[i + 1][j] or dp[i][j + 1]

        return dp[len(s)][len(p)]

    def maxArea(self, height: List[int]) -> int:
        ans, left, right = 0, 0, len(height) - 1
        while left <= right:
            tmp = min(height[left], height[right]) * (right - left)
            ans = max(ans, tmp)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans
