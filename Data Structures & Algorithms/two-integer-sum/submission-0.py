class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vus = {}

        for j in range(len(nums)):
            complement = target - nums[j]
            if complement in vus:
                return [vus[complement], j]
            vus[nums[j]] = j