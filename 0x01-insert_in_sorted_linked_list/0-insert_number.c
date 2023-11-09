#include "lists.h"
#include <stdlib.h>

/**
* insert_node - insert a node in sorted linked list
 * @head: head of the list
 * @number: the number to insert
 * Return: new head
*/
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new, **tmp;

    if(!head)
        return (NULL);
    tmp = head;
    new = malloc(sizeof(listint_t));
    if (!new)
        return(NULL);
    new->n = number;

    while((*tmp) && (*tmp)->n < number)
    {
       tmp = &(*tmp)->next;
    }

    new->next = (*tmp);
    (*tmp) = new;
    return (new);
}
