#include <stdio.h>
#include <string.h>

#define MAX 100

int main(void)
{
    char name[MAX];
    int age;

    printf("Name: ");
    fgets(name, MAX, stdin);
    name[strcspn(name, "\n")] = '\0';

    printf("Age: ");
    scanf("%d", &age);

    printf("%s next birthday you will be %d\n", name, age+1);

    return 0;
}

