class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vus={}
        for i in range(len(nums)):
            but=target-nums[i]
            if but in vus:
                return [vus[but],i]
            vus[nums[i]]=i