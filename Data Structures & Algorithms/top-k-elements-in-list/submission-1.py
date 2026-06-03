from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=Counter(nums)
        ans=sorted(d, key=d.get, reverse=True)
        return ans[:k]