class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def subsetsWithoutDuplicates(nums):
            subsets, curSet = [], []
            helper(0, nums, curSet, subsets)
            return subsets

        def helper(i, nums, curSet, subsets):
            if i >= len(nums):
                subsets.append(curSet.copy())
                return
            
            # decision to include nums[i]
            curSet.append(nums[i])
            helper(i + 1, nums, curSet, subsets)
            curSet.pop()

            # decision NOT to include nums[i]
            helper(i + 1, nums, curSet, subsets)


        return subsetsWithoutDuplicates(nums)