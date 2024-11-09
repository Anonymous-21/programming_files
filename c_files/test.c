#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
  int data;
  struct Node *next;
} Node;

Node *createNode(int data) {
  Node *newNode = (Node *)malloc(sizeof(Node));
  newNode->data = data;
  newNode->next = NULL;
  return newNode;
}

void printList(Node *head) {
  Node *current = head;
  while (current != NULL) {
    printf("%d - ", current->data);
    current = current->next;
  }
  printf("\n");
}

int main(void) {
  Node *head, *second, *third;

  head = createNode(1);

  second = createNode(2);
  head->next = second;

  third = createNode(3);
  second->next = third;

  printList(head);
}
