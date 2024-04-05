class Solution:
    #   =======
    #   Hashmap
    #   =======

    #   Iterate through nums. Return iterated num
    #   and 1st operand if 1st operand exists in
    #   hashmap, else store iterated num in
    #   hashmap
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        op1 = {}    #   op1 ->  idx

        for idx, val in enumerate(nums):
            delta = target - val

            if delta in op1:
                return [op1[delta], idx]

            op1[val] = idx
