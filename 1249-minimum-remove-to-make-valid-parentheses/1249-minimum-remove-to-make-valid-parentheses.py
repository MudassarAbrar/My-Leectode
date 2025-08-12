class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        remove_indices = set()

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)  
            elif ch == ')':
                if stack:
                    stack.pop()  
                else:
                    remove_indices.add(i)  
        remove_indices.update(stack)


        result = []
        for i, ch in enumerate(s):
            if i not in remove_indices:
                result.append(ch)

        return "".join(result)
