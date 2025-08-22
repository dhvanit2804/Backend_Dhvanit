#include<stdio.h>
#include<conio.h>

void main()
{
	int num=10;
	int *p;
	clrscr();

	p = &num;
	printf("\nOriginal Value of num = %d\n",num);

	*p=25;
	printf("\Modified value of num = %d\n",num);

	printf("\Address of num = %u\n",&num);
	printf("\Value stored in pointer (address) = %u\n",p);
	printf("Value at pointer = %d\n",*p);

	getch();

}