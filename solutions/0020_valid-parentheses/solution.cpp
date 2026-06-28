class Solution {
public:
    bool isValid(string s) {
        stack <char> stk;
        for(char c :s){
            if(stk.empty()){
                stk.push(c);
                continue;
            }
            string temp = string(1,stk.top())+string(1,c);
            if(temp == "()" || temp=="[]" || temp=="{}"){
                stk.pop();
            }else{
                stk.push(c);
            }
        }
        return stk.empty();
    }
};