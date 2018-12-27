class Solution {
public:
    int numJewelsInStones(string J, string S) {
        
        int len_S = S.length();
        
        int count = 0;
        
        for(int i=0; i<len_S; i++){
            std::size_t found = J.find(S[i]);
            if(found!=std::string::npos){
                count += 1;
            }
        }
         return count;
    }
};
