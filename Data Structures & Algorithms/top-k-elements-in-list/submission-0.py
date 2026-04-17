from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        cnt = Counter(nums)
        return [x for x, _ in cnt.most_common(k)]
        
