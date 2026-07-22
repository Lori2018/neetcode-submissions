from collections import defaultdict 

class TimeMap:

    def __init__(self):
        # 2d array of (value, )
        self.d = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))
        print(self.d[key])

    def get(self, key: str, timestamp: int) -> str:
        print("start get")
        if key not in self.d:
            return ""
        arr = self.d[key]
        if timestamp < arr[0][0]:
            return ""
        lo = 0
        hi = len(arr) - 1
        while hi - lo > 1:
            print(str(lo) + " " + str(hi))
            mid = (hi + lo) // 2
            if timestamp < arr[mid][0]:
                # elim right side 
                hi = mid - 1
            elif timestamp == arr[mid][0]:
                return arr[mid][1]
            # timestamp > arr[mid][0]
            else:
                lo = mid
        print(str(lo) + " " + str(hi))
        print("end get")
        return arr[lo][1] if arr[hi][0] > timestamp else arr[hi][1]
        # return arr[hi][1] if arr[hi][0] >= timestamp else arr[hi][1]
