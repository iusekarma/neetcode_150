class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            cnt = [0] * 26
            for c in s:
                cnt[ord(c)-ord('a')] += 1
            tcnt = tuple(cnt)
            if tcnt in res:
                res[tcnt].append(s)
            else:
                res[tcnt] = [s]
        return res.values()