class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def getDist(point):
            return math.sqrt(point[0]**2 + point[1]**2)

        coords = []
        heapq.heapify(coords)
        for point in points:
            heapq.heappush(coords, (getDist(point), point))
        
        i = 0
        ans = []
        print(coords)
        while(i<k):
            ans.append(heapq.heappop(coords)[1])
            i+=1
        
        return ans