class Solution:
    def isValid(self, s: str) -> bool:
        # use pop to match the pair

        n = len(s)
        pairs = {
            ")":"(",
            "}":"{",
            "]":"[",
        }

        stack = []

        for c in s:
            if c not in pairs: ## open 
                stack.append(c)
            else: # close
                if len(stack) == 0 or stack[-1] != pairs[c]:
                    return False
                stack.pop()

        return len(stack) == 0