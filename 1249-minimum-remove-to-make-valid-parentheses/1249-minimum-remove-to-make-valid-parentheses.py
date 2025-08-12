class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        remove_indices = set()

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)  # store index of '('
            elif ch == ')':
                if stack:
                    stack.pop()  # match with '('
                else:
                    remove_indices.add(i)  # unmatched ')'

        # Add remaining '(' in stack to removal list
        remove_indices.update(stack)

        # Build the final string without removed indices
        result = []
        for i, ch in enumerate(s):
            if i not in remove_indices:
                result.append(ch)

        return "".join(result)
