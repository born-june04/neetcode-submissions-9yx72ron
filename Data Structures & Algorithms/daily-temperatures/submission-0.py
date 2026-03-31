class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # i = 0, current 30 -> 1
        # i = 1, current 38 -> 4
        # i = 2, current 30 -> 1

        # new list call stack
        # push current temp into stack and compare with new temp with stack top
        # if the new temp is higher than the stack top
        # pop the index of temp and measure the distance

        n = len(temperatures)
        stack = []
        ans = [0]*n

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                ans[idx] = i - idx

            stack.append(i)

        return ans