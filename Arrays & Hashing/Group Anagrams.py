# Approach 1: Hash Map
# Time complexity: O(n * m * logm) for sorting each string (n is the number of strings, m is the average length of each string).
# Space complexity: O(n * m) for storing elements in the hash map (total number of characters across all strings).

class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # approach: Hash Map
    str_map = collections.defaultdict(list)
    for s in strs:  # O(n)
      str_map["".join(sorted(s))].append(s)  # O(m * logm) for sorting
    return [l for l in str_map.values()]  # O(n)
