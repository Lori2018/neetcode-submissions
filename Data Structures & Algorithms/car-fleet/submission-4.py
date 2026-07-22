class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carInfo = [list(pair) + [(target - pair[1]) / pair[0], 1] for pair in zip(speed, position)]
        carInfo = sorted(carInfo, key=lambda row: row[2], reverse=False)
        count = len(position)

        while len(carInfo) > 1: 
            print(carInfo)
            # pop top 2 off of stack & try to combine
            car1 = carInfo.pop()
            car2 = carInfo.pop() 

            speedDiff = car1[0] - car2[0] 
            xt = car2[1] - car1[1]
            if speedDiff != 0 and xt/speedDiff >= 0:
                intersection = car1[0] * xt/speedDiff + car1[1]
                if intersection <= target: 
                    # combine into one car 
                    car3 = car1 if car1[0] < car2[0] else car2
                    carInfo.append(car3)
                    count -= 1
                    print("combined\n")
                    continue
            carInfo.append(car2)
            print("\n")
        return count