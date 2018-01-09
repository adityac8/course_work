#include<iostream>
using namespace std;
int main()
{
    int i,a=0;
    for(i=0;i<10;i++)
    {
        a+=5;
        cout<<a<<" "<<&a<<endl;
    }
    return 0;
}
