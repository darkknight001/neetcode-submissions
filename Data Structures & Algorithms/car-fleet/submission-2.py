class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[pos, s] for s, pos in zip(speed, position)]

        cars.sort(key=lambda x: x[0], reverse=True)
        stack = []
        for car in cars:
            time_taken = (target-car[0])/car[1]
            if not stack or stack[-1]<time_taken:
                stack.append(time_taken)
        
        return len(stack)