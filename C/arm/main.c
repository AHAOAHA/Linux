#include<stdio.h>
#include<wait.h>
#include<stdlib.h>
#include<unistd.h>
int main()
{
  int chose = 0;
  printf("1 :date\n2 :common_div\n3 :is_leapyear\nplease input your chose :");
  fflush(stdout);
  scanf("%d", &chose);
  pid_t id = fork();
  if(-1 == id)
  {
    exit(EXIT_FAILURE);
  }
  else if(0 == id)//child
  {
    switch(chose)
    {
      case 1:execle("./date","/home/ahao/Linux_code/C/arm/");
        break;
      case 2:execle("./common_div", "/home/ahao/Linux_code/C/arm/");
        break;
      case 3:execle("./is_leapyear", "/home/ahao/Linux_code/C/arm/");
        break;
      default:
        printf("bad chose...\n");
        break;
    }

  }
  else//parent
  {
    while(wait(NULL) != id);
  }
  return 0;
}
