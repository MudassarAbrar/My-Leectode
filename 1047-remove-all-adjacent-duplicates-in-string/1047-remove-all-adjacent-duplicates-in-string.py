class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()  # Remove the duplicate
            else:
                stack.append(ch)  # Add the new character
        return "".join(stack)

        