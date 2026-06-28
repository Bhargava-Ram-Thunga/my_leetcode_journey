class Solution {
public:
    bool isLongPressedName(string name, string typed) {
        vector <pair<char,int>> n;
        vector <pair<char,int>> t;
        char curr = name[0];
        int count = 0;
        for(int i = 0;i<name.size();i++){
            if(curr==name[i]){
                count++;
            }else{
                n.push_back({curr,count});
                curr = name[i];
                count = 1;
            }
        }
        n.push_back({curr,count});
        curr = typed[0];
        count = 0;
        for(int i = 0;i<typed.size();i++){
            if(curr==typed[i]){
                count++;
            }else{
                t.push_back({curr,count});
                curr = typed[i];
                count = 1;
            }
        }
        t.push_back({curr,count});
        if (n.size()!=t.size()){
            return false;
        }
        for(int j=0;j<n.size();j++){
            if(n[j].first != t[j].first){
                return false;
            }else if(n[j].second > t[j].second){
                return false;
            }
        }
        return true;
    }
};