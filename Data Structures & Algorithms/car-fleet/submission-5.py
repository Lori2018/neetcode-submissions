class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carInfo = sorted([list(pair) + [(target - pair[1]) / pair[0], 1] for pair in zip(speed, position)], key=lambda row: row[2], reverse=False)
        count = len(position)

        while len(carInfo) > 1: 
            cars = (carInfo.pop(), carInfo.pop())
            if cars[0][0] - cars[1][0] != 0 and (cars[1][1] - cars[0][1])/(cars[0][0] - cars[1][0]) >= 0:
                if cars[0][0] * (cars[1][1] - cars[0][1])/(cars[0][0] - cars[1][0]) + cars[0][1] <= target: 
                    carInfo.append(cars[0] if cars[0][0] < cars[1][0] else cars[1])
                    count -= 1
                    continue
            carInfo.append(cars[1])
        return count