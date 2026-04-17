class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited_dict = {}
        # [3,4,5,6]  target = 7
        for index , num in enumerate(nums):
            target_number = target - num
            if target_number in visited_dict:
                return [visited_dict[target_number] , index]
            else:
                visited_dict[num] = index
        
        
        