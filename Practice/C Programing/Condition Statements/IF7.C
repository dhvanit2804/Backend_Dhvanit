#include<stdio.h>
#include<conio.h>

void main()
{
	int amount,balance = 5000;
	clrscr();

	printf("\nEnter amount to withdraw : ");
	scanf("%d",&amount);

	if(amount % 100 != 0)
		printf("\nEnter amount in multiples of 100");
	else if(amount > balance)
		printf("Insufficient balance");
	else
		printf("Withdrawal successful. Remaining balance = %d",balance - amount);
	getch();
}