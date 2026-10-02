class Solution:
    def isPalindrome(self, ch: str) -> bool:

        ch = [c.lower() for c in ch if c.isalnum()]

        i = 0
        n = len(ch)

        while i < n // 2:
            if ch[i] != ch[n - i - 1]:
                return False

            i += 1

        return True