class Solution:
    def trap(self, height: List[int]) -> int:
        left=[0 for i in range(len(height))]
        right=[0 for i in range(len(height))]
        max1=0
        for i in range(len(height)):
            max1=max(max1,height[i])
            left[i]=max1
        max1=0
        for i in range(len(height)-1,-1,-1):
            max1=max(max1,height[i])
            right[i]=max1
        water=[0 for i in range(len(height))]
        for i in range(len(water)):
            water[i]=min(left[i],right[i])-height[i]
        ans=0
        for i in water:
            ans+=i
        return ans

