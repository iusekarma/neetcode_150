class Solution:
    def reverseBits(self, n: int) -> int:
        out = 0
        for i in range(32):
            out = (out*2) + (n%2)
            n = n//2
        return out