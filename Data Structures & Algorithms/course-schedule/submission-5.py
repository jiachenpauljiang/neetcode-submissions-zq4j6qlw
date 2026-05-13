class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjMap = defaultdict(list)
        for course, pre in prerequisites:
            adjMap[course].append(pre)
        
        state = [0] * numCourses # state tracking. 0 means unvisited, 1 means visiting, 2 means safe

        def dfs(course):
            if state[course] == 2:
                return True
            if state[course] == 1:
                return False
            
            state[course] = 1
            for prereq in adjMap[course]:
                if not dfs(prereq):
                    return False
            state[course] = 2
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        
        # return all(dfs(c) for c in range(numCourses))