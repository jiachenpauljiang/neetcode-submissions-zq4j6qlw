class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjMap = defaultdict(list)
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            adjMap[prereq].append(course)
            indegree[course] += 1
        
        queue = deque([c for c in range(numCourses) if indegree[c] == 0])
        taken = 0

        while queue:
            course = queue.popleft()
            taken += 1

            for neighbor in adjMap[course]:
                # for every course that depends on this course
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return taken == numCourses