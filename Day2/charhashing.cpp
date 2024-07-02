#include<bits/stdc++.h>

using namespace std;
int main()
{
    map<char,int>myMap;

    string s="akshat_khatri_is_a_programmer";

    for (int i = 0; i < s.size(); i++)
    {
        myMap[s[i]]++;
    }

    for(auto it : myMap)
    {
        cout<<it.first<<"-->"<<it.second<<endl;
    }

    cout<<endl;
    for (int i = 0; i < s.size(); i++)
    {
        cout<<s[i]<<"-->"<<myMap[s[i]]<<endl;
    }
    
    
    
    
}