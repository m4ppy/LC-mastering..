#Algorithm 
#the key-point is how to set the delimiter.
#if we just set the delimiter as one special character, it can be showed up in input str. 
#so why dont we add a length of each elements in the first place?
#we can count the char and there no misunderstanding about the encoded string.

#Time Complexity: O(n)
#Space Complexity: O(1)

class Solution:

  def encode(self, strs: List[str]) -> str:
    res = ""
    for s in strs:
      res += str(len(s)) + "#" + s
    return res

  def decode(self, s: str) -> List[str]:
    res = []
    i = 0

    while i < len(s):
      j = i
      while s[j] != "#":
        j += 1
      length = int(s[i:j])
      i = j + 1
      j = i + length
      res.append(s[i:j])
      i = j
        
    return res
