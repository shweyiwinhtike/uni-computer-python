from abc import ABC, abstractmethod

class Transportation(ABC):
    def __init__(self, start_place, end_place, distance) -> None:
        super().__init__()
        self.start_place = start_place
        self.end_place = end_place
        self.distance = distance

    @abstractmethod
    def find_cost(self):
        pass

class Walk(Transportation):
    def __init__(self, start_place, end_place, distance) -> None:
        super().__init__(start_place, end_place, distance)

    def find_cost(self):
        return 0

class Taxi(Transportation):
    def __init__(self, start_place, end_place, distance) -> None:
        super().__init__(start_place, end_place, distance)
    
    def find_cost(self):
        return self.distance * 40

class Train(Transportation):
    def __init__(self, start_place, end_place, distance, station) -> None:
        super().__init__(start_place, end_place, distance)
        self.station = station

    def find_cost(self):
        return 5 * self.station

def main():
    walk = Walk("KMITL", "Lawson at KMITL", 0.6)
    taxi = Taxi("Lawson at KMITL", "Ladkrabang Station", 5)
    train = Train("Ladkrabang Station", "Phayathai Station", 40, 6)
    taxi1 = Taxi("Phayathai Station", "The British Council", 3)
main()

wa1 = Walk("KMITL", "Lawson at KMITL", 0.6)
ta1 = Taxi("Lawson at KMITL", "Ladkrabang Station", 5)
tr1 = Train("Ladkrabang Station", "Payathai Station", 40, 6)
ta2 = Taxi("Payathai Station", "The British Council", 3)

transport = [wa1, ta1, tr1, ta2]
total = 0
for tran in transport:
    fc = tran.find_cost()
    print("Cost:", fc)
    total += fc
    
print("Total:", total)

# Test Output:
"""
Cost: 0.0
Cost: 200.0
Cost: 30.0
Cost: 120.0
Total: 350.0
"""