#include<stdio.h>
#include<unistd.h>
int main()
{
	int i=0;
	char bar[102]={'\0'};
	char* buf="-\\|/";
	while(i<=100){
		bar[i]='#';
		printf("[%-101s][%c][%d%%]\r",bar,buf[i%4],i);
		fflush(stdout);
		usleep(100000);
		++i;
	}
    printf("\n");
	return 0;
}
