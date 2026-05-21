class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()

        curPoint = (0, 0)
        visited.add(curPoint)
        for decision in path:
            if decision == "N":
                curPoint = (curPoint[0], curPoint[1] + 1)
                print(f'decision is N, curPoint is ${curPoint}')
            elif decision == "S":
                curPoint = (curPoint[0], curPoint[1] - 1)
                print(f'decision is S, curPoint is ${curPoint}')
            elif decision == "E":
                curPoint = (curPoint[0] + 1, curPoint[1])
                print(f'decision is E, curPoint is ${curPoint}')
            else:
                curPoint = (curPoint[0] - 1, curPoint[1])
                print(f'decision is W, curPoint is ${curPoint}')
            
            if curPoint in visited:
                return True
            else:
                visited.add(curPoint)
        return False