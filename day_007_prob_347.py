class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1

        freq = [[] for i in range(len(nums)+1)]

        for n,c in counts.items():
            freq[c].append(n)

        out = []
        for v in range(len(freq)-1,0,-1):
            for j in freq[v]:
                out.append(j)
                if len(out) == k:
                    return out
        return out