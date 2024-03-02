class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices={}
        for idx, num in enumerate(nums):
            complement=target-num
            if complement in num_indices:
                return [num_indices[complement], idx]
            num_indices[num]=idx
        return []
