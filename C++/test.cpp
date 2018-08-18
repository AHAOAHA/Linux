#include<iostream>
#include<vector>
#include<string>
using namespace std;
int main()
{
	void* p = nullptr;
	while(1)
	{
		p = malloc(100);
		cout << p << endl;
	}
	return 0;
}
