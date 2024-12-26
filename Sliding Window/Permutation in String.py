# Approach: Sliding Window Fixed Size
# Time Complexity: O(n)
# Space Complexity: O(1)

# Algorithm
# we use Frequency Array for checking valid window.
# array can be compared by O(1).

class Solution:
  def checkInclusion(self, s1: str, s2: str) -> bool:
    if len(s1)>len(s2):
      return False
        
    list_s1=[0]*26
    list_s2=[0]*26

    for i in range(len(s1)):
      list_s1[ord(s1[i])-97]+=1
      list_s2[ord(s2[i])-97]+=1
    
    if list_s1==list_s2:
      return True

    window=len(s1)

    for i in range(window,len(s2)):
      list_s2[ord(s2[i])-97]+=1
      list_s2[ord(s2[i-window])-97]-=1
      if list_s2==list_s1:
        return True
