class Solution:
    def numDistinct(self, s: str, t: str):
        @lru_cache(None)
        def dp(i, j):
            if j == 0: return 1  # Case t = "", there is a valid subsequence which is empty string.
            if i == 0: return 0
            ans = dp(i - 1, j)
            if s[i-1] == t[j-1]:
                ans += dp(i - 1, j - 1)
            return ans
        return dp(len(s), len(t))
      

'''
Let dp(i, j) is the number of distinct subsequences if s[0..i-1] which equal to t[0..j-1].
To compute dp(i, j) there are 2 ways:
dp(i, j) += dp(i-1, j), case our subsequence doesn't contain s[i-1] character.
dp(i, j) += dp(i-1, j-1) in case s[i-1] == t[j-1].
Base case, case t == "" then there is a valid subsequence which is empty string.
'''      
