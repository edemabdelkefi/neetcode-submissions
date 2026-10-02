class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        gauche = 0
        vus = set()
        q = 0
        for droite in range(len(s)):
            while s[droite] in vus:
                vus.remove(s[gauche])
                gauche += 1
            vus.add(s[droite])
            q = max(q, droite - gauche + 1)
        return q