"""
78. Subsets

Approach:
Traverse a decision Tree that contains current element or not -> if it's leaf, add to res.

Time Complexity: O(n * 2^n)   
Space Complexity: O(n) for extra
                  O(2^n) for the output list
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, curset):
            if i >= len(nums):
                res.append(curset.copy())
                return

            curset.append(nums[i])
            dfs(i + 1, curset)
            curset.remove(nums[i])

            dfs(i + 1, curset)
        
        dfs(0, [])

        return res
