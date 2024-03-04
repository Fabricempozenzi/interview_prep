class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq_holder=dict()
        freq_from_dict=[]
        response_holder=[]
        for num in nums:
            if num in num_freq_holder:
                num_freq_holder[num]+=1
            else:
                num_freq_holder[num]=1
        for val in num_freq_holder.values():
            freq_from_dict.append(val)
        freq_from_dict.sort()
        for num in freq_from_dict[-k:]:
            for key in num_freq_holder:
                if(num==num_freq_holder[key] and key not in response_holder):
                    response_holder.append(key)
        return response_holder
