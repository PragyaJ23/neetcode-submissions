class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for ch in s:
            # Opening brackets
            if ch in "([{":
                stack.append(ch)
            # Closing brackets
            else:
                if not stack:
                    return False

                if stack[-1] == mapping[ch]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0