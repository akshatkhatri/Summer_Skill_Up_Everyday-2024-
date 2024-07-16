#include<bits/stdc++.h>
using namespace std;

void nextperma(vector<vector<int>>& ans, vector<int> &hasharr, vector<int> &arr, vector<int>&ds, int &n)
{
    if(ds.size() == n)
    {
        ans.push_back(ds);
        return;
    }

    for (int i = 0; i < n; i++) 
    {
        if(hasharr[i] == 0)
        {
            ds.push_back(arr[i]);
            hasharr[i] = 1;
            nextperma(ans, hasharr, arr ,ds , n);
            hasharr[i] = 0;
            ds.pop_back();
        }
    }
    

}

int main()
{
    vector<vector<int>>ans;
    vector<int>arr={1,2,3,4,5,6};

    int n= arr.size();

    vector<int>hasharr(n);
    vector<int>ds;

    nextperma(ans,hasharr,arr,ds,n);
}