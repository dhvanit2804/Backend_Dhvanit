//Positive Negative Zero
#include<stdio.h>
#include<conio.h>

void main()
{
	int num;
	clrscr();
	printf("\nEnter Number : ");
	scanf("%d",&num);
	if(num>=0)
	{
		printf("\nNumber is Positive");
	}else if(num<=0){
		printf("\nNumber is Negative");
	}
	else{
		printf("\nNumber is Zero");
	}
	getch();
}