class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                a = s[i+1:j+1]
                b = s[i:j]
                return a == a[::-1] or b == b[::-1]
            i += 1
            j -= 1

        return True