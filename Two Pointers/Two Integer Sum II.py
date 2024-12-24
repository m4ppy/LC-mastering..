# Approach: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1) no extra spaces

class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers)-1
    
    while left < right:
      Sum1 = numbers[left] + numbers[right]
      if Sum1 < target:
        left += 1
      elif Sum1 > target:
        right -= 1
      elif Sum1 == target:
        return [left+1, right+1]
    return []
