class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for course, prerequisite in prerequisites:
            preMap[course].append(prerequisite)
        
        visiting = set()

        def dfs(course):
            if course in visiting:
                return False
            
            if preMap[course] == []:
                return True
            
            visiting.add(course)
            for prerequisite in preMap[course]:
                if not dfs(prerequisite):
                    return False
            visiting.remove(course)
            preMap[course] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True