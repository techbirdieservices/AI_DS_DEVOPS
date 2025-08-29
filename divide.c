#include<stdio.h>

int main()
{
    int num1, num2, num3, sum;
    printf("Enter first number: ");
    scanf("%d, &num1");
    printf("Enter second numer: ");
    scanf("%d, &num2");
    printf("Enter third number: ");
    scanf("%d, &num3");
    sum =num1 + num2 + num3;
    printf("The sum of %d and %d and %d is %d\n", num1, num2, num3, sum);
    return 0;
}