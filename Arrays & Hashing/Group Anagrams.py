# Approach 1: Hash Map
# Time complexity: O(n) because we traverse the list once.
# Space complexity: O(n) for storing elements in the hash map.

class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #approach: Hash Map
    str_map = collections.defaultdict(list)
    for s in strs:
      str_map["".join(sorted(s))].append(s)
    return [l for l in str_map.values()]
