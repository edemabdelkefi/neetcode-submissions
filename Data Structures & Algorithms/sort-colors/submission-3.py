class Solution:
    def sortColors(self, nums: List[int]) -> None:
        gauche = 0
        i = 0
        droite = len(nums) - 1
        while i <= droite:
            if nums[i] == 0:
                nums[i], nums[gauche] = nums[gauche], nums[i]
                gauche += 1
                i += 1

            elif nums[i] == 2:
                nums[i], nums[droite] = nums[droite], nums[i]
                droite -= 1

            else:
                i += 1