class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if destination < start:
            destination,start = start,destination
        return min(sum(distance[start:destination]),sum(distance[destination:]+distance[:start]))