from collections import deque
from typing import Deque

n, m = map(int, input().split())

class UnarrivedBus():
    def __init__(self, num, arrival, wait):
        self.num = num
        self.arrival = arrival
        self.wait = wait

class Bus():
    def __init__(self, station, n, end):
        self.number = n
        self.station = station
        self.end = end

        self.update()

    def update(self):
        if self.station.time >= self.end:
            self.waiting = False
        else: 
            self.waiting = True

    def __repr__(self):
        return f"Bus(num: {self.number}, end: {self.end})"

class BusStation():
    def __init__(self, limit: int, target: int):
        self.target = target
        self.stations: Deque[Bus] = deque([ None ] * limit)
        self.waitings: Deque[UnarrivedBus] = deque()
        self.events = set()
        self.time = 0

    def simulation(self):
        while True:
            next_event = min(self.events)
            self.events.remove(next_event)

            time_delta = next_event - self.time
            self.send_time(time_delta)

            before = None

            for i in range(n):
                bus = self.stations[i]
                if bus:
                    bus.update()

                    if bus.waiting is False:
                        if before is None: self.stations[i] = None
                        else:
                            self.stations[i] = None
                            self.stations[before + 1] = bus
                            before = before + 1

                    else: before = i

            if before is None: before = -1

            for i in range(before + 1, n):
                if self.waitings:
                    unarrived_bus = self.waitings[0]
                    bus_num = unarrived_bus.num
                    bus_end = self.time + unarrived_bus.wait

                    if unarrived_bus.arrival <= self.time:
                        self.waitings.popleft()
                        bus = Bus(self, bus_num, bus_end)
                        self.stations[i] = bus
                        self.events.add(bus_end)

                        if bus_num == self.target:
                            print(i + 1)
                            quit()

                    else:
                        break

    def send_time(self, d):
        self.time += d

station = BusStation(n, m)
for i in range(1, m + 1):
    t, p = map(int, input().split())
    unarrived_bus = UnarrivedBus(i, t, p)
    station.waitings.append( unarrived_bus )
    station.events.add( t )

station.simulation()