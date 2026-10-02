class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxi = 0

        while i < j:
            largeur = j - i
            hauteur = min(heights[i], heights[j])

            aire = largeur * hauteur

            maxi = max(maxi, aire)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return maxi