class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjMap = {i: [] for i in range(numCourses)}

        for crs, preR in prerequisites:
            adjMap[crs].append(preR)

        res = []
        visited, cycle = set(), set()

        def dfs(course):
            if course in cycle:
                return False
            
            if course in visited:
                return True
            

            cycle.add(course)
            for pre in adjMap[course]:
                if not dfs(pre):
                    return False
            
            cycle.remove(course)
            visited.add(course)
            res.append(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return res