class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #   Iterate through nums for first operand, then iterate
        #   through nums for second operand excluding iterated
        #   first operands
        nums_len = len(nums)

        for i in range(nums_len):
            for j in range(i + 1, nums_len):
                if nums[i] + nums[j] == target:
                    return [i, j]
