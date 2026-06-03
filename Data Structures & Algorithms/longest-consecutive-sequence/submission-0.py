class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d=set(nums)
        longest=0
        ans=0
        for i in nums:
            if i-1 not in d:
                longest=0
                l=0
                while i+l in d:
                    longest+=1
                    l+=1
                ans=max(ans,longest)
        return ans 
        