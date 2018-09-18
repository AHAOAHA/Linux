#include<stdio.h>
#include<sys/types.h>
#include<unistd.h>
int main()
{
    int pid = fork();
    while(1)
    {
        if(-1 == pid)
        {
            printf("fork error\n");
            return -1;
        }
        else if(0 == pid)
        {
            printf("this is child , pid : %d , ppid : %d\n",getpid(),getppid());
            sleep(1);
        }
        else
        {
            printf("this is father , pid : %d , ppid : %d\n",getpid(),getppid());
            sleep(1);
        }
    }
    return 0;
}
