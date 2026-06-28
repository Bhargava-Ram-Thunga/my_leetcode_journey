class Solution {
public:
    void fibo(vector<int>&v,int n){
        if (n==1){
            return ;
        }
        v.push_back((v[v.size() - 1]) + (v[v.size() - 2]));
        fibo(v, n - 1);
    }
    int fib(int n) {
        vector <int> v1 = {0,1};
        if (n==0){
            return 0;
        }
        if (n==1){
            return 1;
        }
        else{
            fibo(v1,n);
            return v1[v1.size()-1];
        }
    }
};