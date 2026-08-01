class TimeMap:
    # map: key: array of (time, val)
    # set: add to array
    # get: binary search array
    def __init__(self):
        self.m = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key].append((timestamp, value))        

    def get(self, key: str, timestamp: int) -> str:
        arr = self.m[key]
        print(arr, timestamp)
        # find first entry (t, v) st t >= timestamp
        left = 0
        right = len(arr)-1
        while left<right:
            mid = (left+right)//2
            tmid, vmid = arr[mid]
            if tmid == timestamp or (mid == len(arr)-1 and timestamp > tmid):
                return vmid
            elif tmid < timestamp:
                if arr[mid+1][0] > timestamp:
                    return vmid
                left = mid+1
            else:
                right = mid-1
        if right >= 0 and right < len(arr) and arr[right][0] <= timestamp:
            return arr[right][1]
        elif right > 0: # arr[right][0] > timestamp
            return arr[right-1][1]
        else:
            return ""