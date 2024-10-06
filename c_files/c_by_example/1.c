#include <stdio.h>
#include <string.h>

#define MAX 50

int main(void)
{
   char first_name[MAX];

   printf("First Name: ");
   fgets(first_name, MAX, stdin);
   first_name[strcspn(first_name, "\n")] = '\0';

   printf("Hello %s\n", first_name);

   return 0; 
}
