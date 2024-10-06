#include <stdio.h>
#include <string.h>

#define MAX 50

int main(void)
{
    char first_name[MAX], surname[MAX];

    printf("First Name: ");
    fgets(first_name, MAX, stdin);
    first_name[strcspn(first_name, "\n")] = '\0';

    printf("Surname: ");
    fgets(surname, MAX, stdin);
    surname[strcspn(surname, "\n")] = '\0';

    printf("Hello %s %s\n", first_name, surname);

    return 0;
}
