#approach : Counter Module (Hash Map)
#time complexity : O(n)
#space complexity : O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = collections.Counter(nums) # Counter()'s time complexity : O(n)
        for i in nums:
            if count[i] > 1:
                return True
        return False

#approach : Set
#time complexity : O(n)
#space complexity : O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = set()
        for n in nums:
            if n in count:
                return True
            count.add(n)
        return False
