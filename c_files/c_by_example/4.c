#include <stdio.h>

int main(void)
{
    int num1, num2;

    printf("Number: ");
    scanf("%d", &num1);

    printf("Number: ");
    scanf("%d", &num2);

    printf("The total is %d\n", num1 + num2);

    return 0;
}
