class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for val in freq.values():
            if val > 1:
                return True
        return False

s=Solution()
nums=[1,2,3,3]
s.hasDuplicate(nums)
