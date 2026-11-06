class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = zip(position, speed)
        sorted_cars = list(reversed(sorted(cars, key=lambda x: x[0])))

        fleets = 0
        travel_times = []
        for car in sorted_cars:
            travel_times.append( (target - car[0]) / car[1] )

        prev_tt = None

        for tt in travel_times:
            if not (prev_tt):
                prev_tt = tt
            elif prev_tt < tt:
                fleets += 1
                prev_tt = tt

            

        
        return fleets + 1
