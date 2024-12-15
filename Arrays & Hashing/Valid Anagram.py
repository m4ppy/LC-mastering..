#What's the Anagram?
#Anagram: An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.

#approach 1: Sorting
#time complexity: O(nlog n + mlog m)
#space complexity: O(1) 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

#approach 2: Hash Map

#approach 3: Hash Map (Counter Module)
#time complexity: O(n)
#space complexity: O(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = collections.Counter(s)
        countT = collections.Counter(t)
        return countS == countT
