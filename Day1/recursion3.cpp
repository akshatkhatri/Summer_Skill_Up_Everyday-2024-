#include<iostream>
using namespace std;

void foo(int n)
{
    if(n<1)
    return;

    foo(n-1);

    cout<<n<<" ";
}
int main()
{
    int n;
    cout<<"enter the value of n"<<endl;
    cin>>n;
    foo(n);
}