/*
 * 判断Linux下vector的增容方式
 */
#include<vector>
#include<iostream>
using namespace std;
int main()
{
    vector<int> v;
    for(size_t i = 0; i < 1000; ++i)
    {
        size_t tmp = v.capacity();
        v.resize(i);
        if(tmp != v.capacity())
        {
            cout << v.capacity() << endl;
        }
    }
    return 0;
}
