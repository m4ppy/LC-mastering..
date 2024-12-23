class Solution:
  def isPalindrome(self, s: str) -> bool:
    decoded = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    left, right = 0, len(decoded)-1
    while left < right:
      if decoded[left] != decoded[right]:
        return False
      left += 1
      right -= 1
    return True
