#include<bits/stdc++.h>
using namespace std;

void reversearr(vector<int>&arr,int i)
{
    if(i>=arr.size()/2)
    return;

    swap(arr[i],arr[arr.size()-i-1]);
    reversearr(arr,i+1);

}
int main()
{
    vector<int>arr={1,2,3,4,5,6};
    reversearr(arr,0);

    for (int i = 0; i < arr.size(); i++)
    {
        cout<<arr[i]<<" ";
    }
    
}