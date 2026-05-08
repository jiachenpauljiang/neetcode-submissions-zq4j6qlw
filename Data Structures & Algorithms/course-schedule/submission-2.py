class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjMap = {i: [] for i in range(numCourses)}

        for course, prerequisite in prerequisites:
            adjMap[course].append(prerequisite)
        
        visiting = set()
        
        def dfs(course):
            if course in visiting:
                return False
            
            if adjMap[course] == []:
                return True
            visiting.add(course)
            
            for prerequisite in adjMap[course]:
                if not dfs(prerequisite):
                    return False
            
            adjMap[course] = []
            visiting.remove(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True