#include<stdio.h>
#include<unistd.h>
int main()
{
    printf("This is a proc\n");
    execl("/bin/ls","ls","-l",NULL);
    printf("This is end\n");
    return 0;
}
