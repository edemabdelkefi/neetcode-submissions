class Solution:
    def mySqrt(self, x: int) -> int:
        i=0
        while not i**2<=x<(i+1)**2:
            i=i+1
        return i