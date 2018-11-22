#include<stdio.h>
#include<stdlib.h>
#include<sys/types.h>
#include<sys/wait.h>
#include<unistd.h>
#include<string.h>
int main()
{
    int fd[2];
    if(pipe(fd) != 0)
    {
        printf("管道创建失败!\n");
        exit(-1);
    }
    pid_t id = fork();
    char buf[64];
    if(-1 == id)
        exit(-1);
    else if(0 == id)
    {
        int i = 0;
        close(fd[0]);//关闭读端
        strcpy(buf, "hello father!\n");
        while(1)
        {
            write(fd[1],buf,strlen(buf));
            printf("%d\n",i++);
        }
        close(fd[1]);//关闭写端
    }
    else
    {
        close(fd[1]);//关闭写端
        while(1)
        {
            read(fd[0],buf,14 * 20);
            printf("%s", buf);
            sleep(3);
        }

        while(wait(NULL) != id);
        close(fd[0]);//关闭读端
    }
    return 0;
}
