# Approach: Stack
# Time Complexity: O(n) for traversing input list once
# Space Copmlexity: O(n) for stack list

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        stack = []
        answer = [0] * l

        # Monotonic Decreasing Stack
        # the elements of stack are followed on decreasing order 
        # and if the append value is bigger than stack's top value, pop it to make it's order correctly.

        for i in range(l):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                s = stack.pop()    
                
                # the key point of this stack problem.
                # current index - stack[-1] index
                answer[s] = i - s

            stack.append(i)
        return answer
