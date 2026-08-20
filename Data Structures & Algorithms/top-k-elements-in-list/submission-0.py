from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return ([x[0] for x in count.most_common(k)])
nums = [1, 2, 2, 3, 3]
k = 2
s=Solution()
s.topKFrequent(nums,k)