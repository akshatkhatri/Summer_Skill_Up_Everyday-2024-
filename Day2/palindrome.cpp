#include<bits/stdc++.h>
using namespace std;

bool ispalindrome(string s,int i)
{
    if(i>=s.length()/2)
    return true;
    
    if(s[i]!=s[s.length()-i-1])
    return false;

    return ispalindrome(s,i+1);
    

}
int main()
{
    string s="MadaM";
    string ns="madsm";
    
    bool ans1=ispalindrome(s,0);
    bool ans2=ispalindrome(ns,0);

    cout<<ans1<<endl<<ans2;
}