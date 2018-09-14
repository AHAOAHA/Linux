#include<iostream>
int main()
{
    int num = 100;
    int i = 0;
    std::cout << "100~200之间的质数：";
    for(num = 100 ; num <= 200 ; ++num)
    {
        for(i = 2 ; i <= num ; ++i)
        {
            if(0 == num % i && i != num)
                break;
            if(i == num)
                std::cout<< num << " ";
        }
    }
    std::cout<<std::endl;
    return 0;
}
