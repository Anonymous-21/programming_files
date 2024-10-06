#include <stdio.h>

int main(void)
{
    int num1, num2, num3;

    printf("Number: ");
    scanf("%d", &num1);
    printf("Number: ");
    scanf("%d", &num2);
    printf("Number: ");
    scanf("%d", &num3);

    printf("The answer is %d\n", (num1+num2)*num3);

    return 0;
}
