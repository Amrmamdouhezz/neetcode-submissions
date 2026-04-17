from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_cnt = Counter(nums)
        for cnt in nums_cnt.values():
            if cnt > 1:
                return True
        return False
       

        