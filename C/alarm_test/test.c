#include<stdio.h>
#include<unistd.h>
int main()
{
    
    int ret = alarm(100);

    while(1)
    {
        ret  = alarm(10);
        printf("%d\n", ret);
        sleep(1);
    }
    return 0;
}
