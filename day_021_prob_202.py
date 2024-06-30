class Solution:
    def isHappy(self, n: int) -> bool:
        v = set()
        while n not in v:
            v.add(n)
            n = self.ss(n)
            if n == 1:
                return True
        return False
     
    def ss(self, n):
        output = 0
        while n:
            output += (n % 10) ** 2
            n = n // 10
        return output