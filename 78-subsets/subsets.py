class Solution:
    def subsetsUtil(self,index: int, nums: List[int], result: list[int], final: list[list[int]]) -> List[List[int]]:
        if index >= len(nums):
            final.append(result)
            return final

        copy = result.copy()
        copy.append(nums[index])
        
        self.subsetsUtil(index=index+1, nums=nums, result=copy, final=final)
        self.subsetsUtil(index=index+1, nums=nums, result=result, final=final)
        
        return final


    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        return self.subsetsUtil(index=0, nums=nums, result=[], final=[])

        