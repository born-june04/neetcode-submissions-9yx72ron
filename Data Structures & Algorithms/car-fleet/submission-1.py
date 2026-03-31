class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1/3 = 1-> 4 -> 7 -> 10
        # 4/2 = 4 -> 6 -> 8 -> 10

        ## (10-1)/3 = 3
        ## (10-4)/2 = 3

        #4/2 = 4 - 6 - 8 - 10
        #1/2 = 1 - 3 - 5 - 7 - 9 - 10
        #0/1 = 0 - 1- 2- 3- 4- ..
        #7/1 = 7 - 8 - 9 - 10

        ## (10-4)/2 = 3
        ## 10-1/2 = 4.5
        ## 10-0/1 = 10
        ## 10-7/1 = 3

        ## so we can use target - position / speed = eta
        ## match eta

        n = len(position)
        pairs = sorted(zip(position, speed), reverse=True)
        stack = []

        for pos, spd in pairs:
            eta = (target - pos) / spd
            if not stack or eta > stack[-1]:
                stack.append(eta)
        
        return len(stack)
        