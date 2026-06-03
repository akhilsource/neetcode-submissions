from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        c = defaultdict(list)
        for i in strs:
            key = tuple(sorted(i))  
            c[key].append(i)
        return list(c.values())     