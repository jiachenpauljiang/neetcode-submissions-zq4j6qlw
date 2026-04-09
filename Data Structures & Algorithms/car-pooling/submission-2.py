class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        changeOfPassengers = [0] * 1001

        for numOfPass, start, end in trips:
            changeOfPassengers[start] += numOfPass
            changeOfPassengers[end] -= numOfPass
        
        currentNumOfPassengers = 0
        for i in range(len(changeOfPassengers)):
            currentNumOfPassengers += changeOfPassengers[i]
            if currentNumOfPassengers > capacity:
                return False
        return True