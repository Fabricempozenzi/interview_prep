class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        newList=set()
        for num in nums:
            if num in newList:
                return True
            else:
                newList.add(num)
        return False

    
       

       
        
