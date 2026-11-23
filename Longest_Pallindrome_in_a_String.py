class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        max_length = 0

        for i in range(len(s)):
            for left, right in ((i, i), (i, i + 1)):
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    length = right - left + 1

                    if length > max_length:
                        start = left
                        max_length = length

                    left -= 1
                    right += 1

        return s[start:start + max_length]
