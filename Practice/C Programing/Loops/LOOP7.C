//Count Digits in a Number
#include<stdio.h>
#include<conio.h>

void main()
{
	int num,count=0;
	clrscr();
	printf("\nEnter N : ");
	scanf("%d",&num);
	if(num==0){
		count = 1;
	}
	else{
		while(num!=0){
			num = num / 10;
			count++;
		}
	}
	printf("\nTotal Digit = %d",count);
	getch();
}