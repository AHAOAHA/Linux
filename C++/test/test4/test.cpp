#include<stdio.h>
#include<unistd.h>
int main()
{
    size_t id=fork();
    if(0==id)
    {
        while(1){
        //printf("this is proc first,pid=%d,ppid=%d\n",getpid(),getppid());
        sleep(1);
        }
    }
    else
    {
        while(1){
        //printf("this is proc second,pid=%d,ppid=%d\n",getpid(),getppid());
        sleep(1);
        }
    }
    return 0;
}
