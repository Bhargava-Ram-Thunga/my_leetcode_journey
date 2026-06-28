class Solution {
public:
    int arrangeCoins(int n) {
        int i =1;
        for(i=1;i<=n;i++){
            if((long(i)*long(i+1)/2) > n){
                return i-1;
            }
        }
        return i-1;
    }
};