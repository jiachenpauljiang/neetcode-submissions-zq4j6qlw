class TimeMap:

    def __init__(self):
        self.keystore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keystore:
            self.keystore[key] = {}
        
        if timestamp not in self.keystore[key]:
            self.keystore[key][timestamp] = []
        self.keystore[key][timestamp].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keystore:
            return ""
        seen = 0

        for time in self.keystore[key]:
            if time <= timestamp:
                seen = max(seen, time)
        
        if seen == 0:
            return ""
        else:
            return self.keystore[key][seen][-1]