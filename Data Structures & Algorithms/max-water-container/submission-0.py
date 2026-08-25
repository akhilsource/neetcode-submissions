class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        max1=0
        while l<r:
            height=min(heights[l],heights[r])
            breadth=r-l
            area=height*breadth
            max1=max(max1,area)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return max1
