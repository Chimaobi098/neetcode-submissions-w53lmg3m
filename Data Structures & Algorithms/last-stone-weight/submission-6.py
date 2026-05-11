class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg_stones = [-s for s in stones]
        heapq.heapify(neg_stones)

        while len(neg_stones) > 1:
            # first vlaue
            y = heapq.heappop(neg_stones) 
        #    second value
            x = heapq.heappop(neg_stones)

            if x == y:
                continue
            else:
                new_input = (y - x)
                heapq.heappush(neg_stones, new_input)
        
        if len(neg_stones) > 0:
            return -neg_stones[0]
        else:
            return 0




        