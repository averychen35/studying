class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            counts = [0] * 26
            for c in s:
                counts[ord(c)-ord("a")] += 1
            res[tuple(counts)].append(s) # must use a tuple bc dictionary key must be immutable
        return list(res.values())

