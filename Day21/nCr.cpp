#include<bits/stdc++.h>

using namespace std;

int nCr(int n, int r){
        long long int res = 1;
         long long int mod = (int)pow(10, 9) + 7;
        for(long long int i = 0; i < r; i++)
        {
            res = res * (n - i);
            res = res / (i + 1);
        }
        
        
        
        return res % mod;
    }
int main()
{
    int n = 10;
    int r = 3;
    int res = nCr(n,r);
    cout<<res<<endl;
}