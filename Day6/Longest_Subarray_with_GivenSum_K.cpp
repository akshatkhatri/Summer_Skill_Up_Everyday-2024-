#include<bits/stdc++.h>
using namespace std;

void find_subarrays_BruteForce(vector<int>arr,int val)
{
    int sum = 0;
    int len = 0;

    for (int i = 0; i < arr.size(); i++)
    {
        for(int j = i; j < arr.size(); j++)
        {
            sum = 0;
            for (int k = i; k <= j; k++)
            {
                sum = sum + arr[k];
                cout<<arr[k]<<" ";
            }

            if(sum == val)
            {
                len = max(len,j-i+1);
            }
            cout<<endl;
            
        }
    }

    cout<<endl<<"FINAL ANSWER IS ->"<<len<<endl;
    
}

void find_subarrays_sum_better_BruteForce(vector<int>arr,int val)
{
    int sum = 0;
    int len = 0;

    for (int i = 0; i < arr.size(); i++)
    {
        sum = 0;
        for(int j = i; j < arr.size(); j++)
        {
            sum = sum + arr[j];
            if(sum == val)
            {
                len = max(len,j-i+1);
            }
            
        }
    }

    cout<<endl<<"FINAL ANSWER IS ->"<<len<<endl;
    
}

void find_subarrays_sum_better_PrefixSum(vector<int>arr, int val)
{
    unordered_map<long long int,int> prefix_sum;
    int preSum = 0;
    int len=0;
    // Created a Prefix Sum array 
    for (int i = 0; i < arr.size(); i++)
    {
        preSum = preSum + arr[i];

        if (preSum == val)
        {
            len = max(len,i+1);
        }

        if(prefix_sum.find(preSum - val) != prefix_sum.end())
        {
            len = max(len, i- prefix_sum[preSum - val]);
        }

        if(prefix_sum.find(preSum) == prefix_sum.end()){
            prefix_sum[preSum] = i;
        } // this line makes the array [2,0,0,3] work for k=5 , do dry run yourself
    }

    // Calculating the length of the largest subarray
    cout<<"FINAL PREFIX ANSWER -> "<<len<<endl;
    
}

void find_subarrays_sum_Optimal_OnlyforPositives_TwoPointer(vector<int>arr, int val)
{
    int i=0;
    int j=0;
    int sum = 0;
    int len=0;

    while (i < arr.size())
    {
        sum = sum + arr[j];
        if(sum == val)
        {
            len = max(len,j-i+1);
        }

        i++;
    }
    
}
int main()
{
    vector<int>arr={1,2,2,1,1,1,1,4,2,3};

    find_subarrays_BruteForce(arr,3);
    find_subarrays_sum_better_BruteForce(arr,3);
    find_subarrays_sum_better_PrefixSum(arr,3);
    find_subarrays_sum_Optimal_OnlyforPositives_TwoPointer(arr,3);
}