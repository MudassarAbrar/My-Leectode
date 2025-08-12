class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        count = 0  # counts unmatched closing brackets
        matching = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in "({[":  # Opening bracket
                stack.append(ch)
            else:  # Closing bracket
                if stack and stack[-1] == matching[ch]:
                    stack.pop()  # Matched, remove from stack
                else:
                    count += 1  # No match, needs fixing
        
        # Remaining opening brackets in stack need closing
        return count + len(stack)
