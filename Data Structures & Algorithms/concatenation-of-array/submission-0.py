class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        L=nums
        for i in range(len(nums)):
            L.append(nums[i])
        return L
