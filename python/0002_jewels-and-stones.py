class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        
        S_unique = [x for x in S]
        S_unique = list(S_unique)
        
        
        count = 0
        
        for ele in S_unique:
            for temp in [y for y in J]:
                if ele == temp:
                    count += 1
                else:
                    continue
                    
        return count
