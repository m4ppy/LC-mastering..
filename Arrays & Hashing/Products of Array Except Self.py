#Approach: Prefix & Suffix
#Time Complexity: O(n)
#Space Complexity: O(1) there are no extra spaces without output array.

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    #there are another way to initialize the result list. it's just make result empty list. But we don't do that. Why? 
    #because if we do that, we have append the to the result while traversal, and it's not efficient. 
    result = [1] * len(nums)  #this avoids appending to a list during iteration.

    prefix_num = 1
    for i in range(len(nums)):
      result[i] = prefix_num
      prefix_num *= nums[i]
      
    postfix_num = 1
    for i in range(len(nums)-1, -1, -1):
      result[i] = result[i] * postfix_num
      postfix_num *= nums[i]
        
    return result
