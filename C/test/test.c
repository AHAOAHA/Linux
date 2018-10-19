#include<unistd.h>
#include<wait.h>
#include<stdlib.h>
#include<stdio.h>
#include<string.h>
int main()
{
    int pipfd[2];
    pipe(pipfd);
    //printf("%d %d",pipfd[0],pipfd[1]);
    pid_t id = fork();
    if(0 == id)
    {
        int i = 10;
        close(pipfd[0]);
        char* buf = "hello\n";
        while(i--)
        {
            write(pipfd[1],buf,strlen(buf));
            sleep(1);
        }
        close(pipfd[1]);
        exit(0);
    }
    else
    {
        close(pipfd[1]);
        char str[1024];
        while(1)
        {
            ssize_t s = read(pipfd[0],str,sizeof(str) - 1);
            printf("%s",str);
            if(s = 0)
            {
                break;
            }
        }
        wait(id);
    }
    return 0;
}
