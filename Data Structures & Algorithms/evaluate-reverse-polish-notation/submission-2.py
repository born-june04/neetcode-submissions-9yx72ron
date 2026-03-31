class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # we do the calculation with the previous number whenever we see the notation
        # 1,2,+ -> 3
        # 3,3,* -> 9
        # 9,4,- -> 5

        n = len(tokens)
        stack = []

        for token in tokens:
            if token in {"+","-","*","/"}:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    ans = a+b
                elif token == "-":
                    ans = a-b
                elif token == "*":
                    ans = a*b
                else:
                    ans = a/b
                stack.append(int(ans))
            else:
                stack.append((int(token)))

        return stack[-1]