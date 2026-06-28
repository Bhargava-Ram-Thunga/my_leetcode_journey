class Solution {
public:
    string makeGood(string s) {
        stack <char> stk;
        for (int i=0;i<s.size();i++){
            if(stk.empty()){
                stk.push(s[i]);
                continue;
            }
            if((isupper(stk.top())&& islower(s[i]) && (char)toupper(s[i])==stk.top()) || (islower(stk.top())&& isupper(s[i]) && (char)tolower(s[i])==stk.top()) ){
                stk.pop();
                continue;
            }
            else{
                stk.push(s[i]);
            }
        }
        string res = "";
        while(!stk.empty()){
            res = stk.top()+res;
            stk.pop();
        }
        return res;
    }
};