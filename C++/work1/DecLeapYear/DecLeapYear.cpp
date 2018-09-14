#include<iostream>
int main()
{
    int year = 1000;
    std::cout << "1000~2000之间的闰年：";
    for(year = 1000 ; year <= 2000 ; ++year)
    {
        if(0 == year % 100)
        {
            if(0 == year % 400)
                std::cout << year <<" ";
        }
        else
        {
            if(0 == year % 4 && 0 != year % 100)
                std::cout << year << " ";
        }
    }
    std::cout<<std::endl;
    return 0; 
}
