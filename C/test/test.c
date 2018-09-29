#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
void Hello(int i)
{
    printf("hello Linux   %d\n",i);
}
int main()
{
    pid_t id=fork();
    if(-1==id)
    {
        printf("error\n");
        exit(1);
    }
    else if(0 == id)//子进程
    {
        while(1)
        {
            sleep(2);
        }
    }
    else
    {
        while(1)
        {
            sleep(1);
        }
    }
    return 0;
}
