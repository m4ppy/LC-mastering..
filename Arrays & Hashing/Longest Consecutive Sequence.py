# Approach: Hash Set

# Time Complexity: O(n)
# Space Complexity: O(n) for hash set

class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    num_set = set(nums)
    longest = 0
    #traverse the list once
    for num in num_set:
      if (num - 1) not in num_set:
        length = 1
        while (num + length) in num_set:
          length += 1
        longest = max(length, longest)
    return longest
