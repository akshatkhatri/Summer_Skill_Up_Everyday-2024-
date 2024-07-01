#include<iostream>
using namespace std;

void foo(int i,int n)
{
    if(i>n)
    return;

    foo(i+1,n);
    cout<<i<<" ";
}
int main()
{
    int n,i=1;
    cout<<"enter the value of n"<<endl;
    cin>>n;
    foo(i,n);
}