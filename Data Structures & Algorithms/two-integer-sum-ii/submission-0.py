class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left=0
        right=len(nums)-1
        while left<right:
            total=nums[left]+nums[right]
            if total==target:
                return [left+1,right+1]
            elif total<target:
                left+=1
            else:
                right-=1
s=Solution()
nums=[1,2,3,4]
target=3
s.twoSum(nums,target)
        