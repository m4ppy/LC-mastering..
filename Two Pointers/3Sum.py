# Approach: Two Pointers
# Time Complexity: O(n²)
# Spcae Complexity: O(1)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, n in enumerate(nums):
            if n>0:
                break
            if i>0 and n == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                Sum1 = n + nums[left] + nums[right]
                if Sum1 > 0:
                    right -= 1
                elif Sum1 < 0:
                    left += 1
                else:
                    result.append([n, nums[left], nums[right]]) 
                    right -= 1
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1 
        return result
