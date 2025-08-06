//Check if a number is palindrome
#include<stdio.h>
#include<conio.h>

void main()
{
	int num,temp,rev=0,digit;
	clrscr();
	printf("\nEnter Number : ");
	scanf("%d",&num);
	temp = num;
	while(temp!=0){
		digit = temp % 10;
		rev = rev * 10 + digit;
		temp /= 10;
	}
	if(num == rev)
	{
		printf("\nPalindrome");
	}else{
		printf("\nNot Palindrome");
	}
	getch();
}
