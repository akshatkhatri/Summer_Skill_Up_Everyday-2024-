#include<bits/stdc++.h>
using namespace std;

void reversearr(vector<int>&arr,int left,int right)
{
    if(left>=right)
    return;
    
    swap(arr[left],arr[right]);
    reversearr(arr,left+1,right-1);
}
int main()
{
    vector<int>arr={1,2,3,4,5};
    reversearr(arr,0,4);

    for (int i = 0; i < 5; i++)
    {
        cout<<arr[i]<<" ";
    }
    
}