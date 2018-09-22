#include<iostream>
void sum()
{
    int i = 0;
    int sum = 0;
    for(; i<=100;i++)
    {
        sum += i;
    }
    std::cout<<"res"<<sum<<std::endl;
}
int main()
{
    std::cout<<"debug begin"<<std::endl;
    sum();
    std::cout<<"debug end"<<std::endl;
    return 0;
}
