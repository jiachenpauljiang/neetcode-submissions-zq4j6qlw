class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        miss = 0

        while students and sandwiches:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                miss = 0
            else:
                miss += 1
                students.append(students.pop(0))
            if miss == len(students):
                break
        return miss