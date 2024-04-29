import time

class Station():
    def __init__(self, name, temp) -> None:
        self.name:str = name
        self.min:float = temp
        self.mean:float = temp
        self.max:float = temp
        self.cnt:int = 1
        pass

    def __repr__(self) -> str:
        return f"{self.name}={self.min}/{round(self.mean/self.cnt, 1)}/{self.max}"

stations:dict[str, Station] = {}

def solution():
    with open("../../../data/measurements.txt", "r", encoding="utf-8") as f:
        for i in f.read().split("\n"):
            station_name, temp = i.split(";")
            temp = float(temp)
            
            if station_name in stations:
                stations[station_name].mean += temp
                stations[station_name].min = min(stations[station_name].min, temp)
                stations[station_name].max = max(stations[station_name].max, temp)
                stations[station_name].cnt += 1
            else:
                stations[station_name] = Station(station_name, temp)
            
    print("{", end="")
    print(", ".join(map(lambda x:str(x[1]), stations.items())))
    print("}")

def main():
    start_time = time.time()
    solution()
    print(time.time() - start_time)

if __name__ == "__main__":
    main()