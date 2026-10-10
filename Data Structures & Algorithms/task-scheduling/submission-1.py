class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        
        arr = [-f for f in freq.values()]
        heapq.heapify(arr)

        time = 0
        q = deque() #pairs(-cnt, idletime)

        while arr or q:
            time+=1
            if arr:
                curr = heapq.heappop(arr)
                curr+=1
                if curr<0:
                    q.append((curr, time+n))

            if q and q[0][1]==time:
                cnt,_=  q.popleft()
                heapq.heappush(arr, cnt)
        
        return time


