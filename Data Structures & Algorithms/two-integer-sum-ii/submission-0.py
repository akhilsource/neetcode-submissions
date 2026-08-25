class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binary_search(left,target):
            right=len(numbers)-1
            while left<=right:
                mid=(left+right)//2
                if numbers[mid]==target:
                    return mid
                elif numbers[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
            return -1
        for i in range(len(numbers)):
            dif=target-numbers[i]
            e=binary_search(i+1,dif)
            if e!=-1:
                return [i+1,e+1]
        return [-1,-1]