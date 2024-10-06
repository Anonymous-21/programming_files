#include <stdio.h>

int main(void)
{
    int total, eaten;

    printf("Total pizza slices: ");
    scanf("%d", &total);
    printf("Pizza slices eaten: ");
    scanf("%d", &eaten);

    printf("Remaining Slices: %d\n", total - eaten);

    return 0;    
}
