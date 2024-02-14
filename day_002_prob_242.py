class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            d_s = {}
            for i in s:
                if i in d_s: d_s[i] += 1
                else: d_s[i] = 1
            for j in t:
                if j in d_s:
                    if d_s[j] - 1 == 0:
                        del d_s[j]
                    else:
                        d_s[j] -= 1
                else:
                    return False
            if not d_s:
                return True
        else:
            return False