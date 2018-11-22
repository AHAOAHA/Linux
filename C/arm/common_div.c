#include<stdio.h>
int main()
{
  int pos = 0;
  int num1 = 0;
  int num2 = 0;
  printf("please input two num\n");
  printf("num1: ");
  fflush(stdout);
  scanf("%d", &num1);
  printf("num2: ");
  fflush(stdout);
  scanf("%d", &num2);
  pos = num1 > num2 ? num2 : num1;

  for(pos; pos > 0; --pos)
  {
    if(num1 % pos == 0 && num2 % pos == 0)
    {
      printf("common_div is %d...\n", pos);
      break;
    }
  }
  return 0;
}
