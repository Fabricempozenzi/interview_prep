class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        newList=list(strs)
        word_indices_pair={}
        respo_List=[]
        for i in range(len(newList)):
            temp=list(newList[i])
            temp.sort()
            temp="".join(temp)
            newList[i]=temp
        for i in range(len(newList)):
            if newList[i] in word_indices_pair:
                word_indices_pair[newList[i]].append(i)
            else:
                word_indices_pair[newList[i]]=[i]
        for word in word_indices_pair:
            temp=[]
            for index in word_indices_pair[word]:
                temp.append(strs[index])
            respo_List.append(temp)
        return respo_List
            
            

            
        
                

        
        



        


