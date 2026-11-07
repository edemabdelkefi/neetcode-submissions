class Solution:
    from math import gcd
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        for start in range(self.gcd(n,k)):
            i = start
            m = (i + k) % n
            while m != start:
                nums[start], nums[m] = nums[m], nums[start]
                i = m
                m = (i + k) % n