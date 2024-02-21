class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        s_set = {s[0]}
        count = 1
        max_count = 1
        l = 0
        for r in range(1,len(s)):
            while s[r] in s_set:
                s_set.remove(s[l])
                l += 1
                count -= 1
            s_set.add(s[r])
            count += 1
            max_count = max(count,max_count)
        return max_count