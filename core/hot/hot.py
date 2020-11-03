from typing import List


class Hot:

    # 19.IsMatch 正则表达式匹配
    def isMatch(self, s: str, p: str) -> bool:
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

    # 11. 盛最多水的容器
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

    # 17. 电话号码的字母组合
    def letterCombinations(self, digits: str) -> List[str]:
        ans=[]
        if not digits or len(digits)<1:
            return ans

        nts = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        def dfs(cur:str,idx:int):
            if idx == len(digits):
                ans.append(cur)
                return

            num = int(digits[idx])
            value = nts[num]
            for v in value:
                dfs(cur+ v,idx+1)

        dfs('',0)
        return ans

def main():
    hot = Hot()
    print(hot.letterCombinations("23"))

if __name__ == "__main__":
    main()