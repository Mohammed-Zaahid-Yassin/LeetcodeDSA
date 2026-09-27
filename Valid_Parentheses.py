class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:  # closing bracket
                # Stack empty or top doesn't match
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:  # opening bracket
                stack.append(char)
        
        # Valid only if all brackets were matched
        return len(stack) == 0
      
