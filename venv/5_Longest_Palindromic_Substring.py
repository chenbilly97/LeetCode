class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        dp = [[False] * (length + 1) for _ in range(length + 1)]
        res = ""
        longestLen = 0;
        for i in reversed(range(length)):
            for j in range(i, length):
                if (s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1] == True)):
                    dp[i][j] = True
                    if (longestLen < j - i + 1):
                        longestLen = j - i + 1
                        res = s[i:j + 1]
        return res
