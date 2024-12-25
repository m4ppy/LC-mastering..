# Approach: Sliding Window
# Time Complexity: O(n) n is the length of the string
# Space Complexity: O(m) m is the total number of unique characters in the string.

# we neet to find sliding window that matches the substring that has most repeating characters.
# hash map counts the current value of substring's number of elements.

class Solution:
  def characterReplacement(self, s: str, k: int) -> int:
    count = collections.defaultdict(int)
    res = 0

    l = 0
    maxf = 0
    for r in range(len(s)):
      count[s[r]] += 1
      maxf = max(count[s[r]], maxf)

      while (r - l + 1) - maxf > k:
        count[s[l]] -= 1
        l += 1

      res = max((r - l + 1), res)
    return res

# Optimal Version
# remove the use of max() function.

class Solution:
  def characterReplacement(self, s: str, k: int) -> int:
    count = collections.defaultdict(int)

    l = 0
    maxf = 0

    # enumerate() doesn't reduce runtime.
    for r, c in enumerate(s):
      count[c] += 1
      if count[c] > maxf:
        maxf = count[c]

      while (r - l + 1) - maxf > k:
        count[s[l]] -= 1
        l += 1

    return len(s) - l
