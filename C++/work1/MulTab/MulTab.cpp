#include<iostream>
#include<iomanip>
int main()
{
    int i = 0;
    int j = 0;
    for(i = 0; i < 10 ; ++i)
    {
        for (j = 0;j < i; ++j) 
        {
            std::cout << i << "*" << j << "=" << std::left << std::setw(2) << i * j << "  ";
        }
        std::cout<<std::endl;
    }
    return 0;
}
