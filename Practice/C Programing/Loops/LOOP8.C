//Sum of digits of number
#include<stdio.h>
#include<conio.h>

void main()
{
	int num,sum=0;
	clrscr();
	printf("\nEnter number : ");
	scanf("%d",&num);

	if(num == 0){
		sum=0;
	}else{
		while(num!=0){
			sum += num%10;
			num = num / 10;
		}
	}
	printf("\nSum of digits = %d",sum);
	getch();
}