#include<iostream>
using namespace std;

int count=0;
void foo()
{
    if(count==4)
    {
        return;
    }

    count++;
    cout<<"current count value is "<<count<<endl;
    foo();
    count--;
    cout<<"exiting with value of count"<<count<<endl;
}
int main()
{
    foo();
}