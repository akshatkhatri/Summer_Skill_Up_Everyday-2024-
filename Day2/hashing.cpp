#include<bits/stdc++.h>

using namespace std;
int main()
{
    map<int,int>myMap;

    vector<int>arr={1,5,6,7,2,2,3,5,1,4,4,9,3,2};

    for (int i = 0; i < arr.size(); i++)
    {
        myMap[arr[i]]++;
    }

    // for(auto it : myMap)
    // {
    //     cout<<it.first<<"-->"<<it.second<<endl;
    // }

    cout<<endl;
    for (int i = 0; i < arr.size(); i++)
    {
        cout<<arr[i]<<"-->"<<myMap[arr[i]]<<endl;
    }
    
    
    
    
}