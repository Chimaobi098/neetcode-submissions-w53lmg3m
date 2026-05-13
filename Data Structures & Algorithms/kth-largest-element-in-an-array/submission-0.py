class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # new_list = list(set(nums))

        minHeap = nums

        heapq.heapify(minHeap)

        while len(minHeap) > k:
            heapq.heappop(minHeap)
        
        return minHeap[0]


        