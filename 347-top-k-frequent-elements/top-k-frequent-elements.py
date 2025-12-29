import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}

        for num in nums:
            freq, key = hash_map.get(num, (0, num))
            hash_map[num] = freq-1, key

        freqency_list = list(hash_map.values())
        heapq.heapify(freqency_list)


        final_list = []
        
        for i in range(k):
            _, num = heapq.heappop(freqency_list)
            final_list.append(num)

        return final_list



        

        