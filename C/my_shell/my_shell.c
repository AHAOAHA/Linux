
#include<stdio.h>
#include<unistd.h>
#include<string.h>
#include<wait.h>
#include<stdlib.h>
#define MAX_CMD 1024
#define MAX_ARGV 20
void my_shell(char cmd[])
{
    pid_t id = fork();
    if(-1 == id)
    {
        exit(0);
    }
    else if(0 == id)
    {
        system(cmd);
    }
    else
    {
        while(id != wait(NULL));
    }
}
int main()
{
    char cmd[MAX_CMD]={'\0'};
    while(1)
    {
        printf("[ahao@AHAOAHA ~]$ ");
        fgets(cmd, sizeof(cmd), stdin);
        my_shell(cmd);
    }
    return 0;
}
