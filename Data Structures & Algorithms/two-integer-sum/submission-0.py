class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevHashSet = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevHashSet:
                return [prevHashSet[diff],i]
            prevHashSet[n] = i
        return

        