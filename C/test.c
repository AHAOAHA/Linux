#include<iostream>
#include<string.h>
using namespace std;
int main()
{
	char* p = "\x111";
    cout<<strlen(p)<<endl;
    cout<<*p<<endl;
	return 0;
}
