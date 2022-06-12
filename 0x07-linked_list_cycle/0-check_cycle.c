#include "lists.h"


/**
 * check_cycle - check cycle in linked list
 * @list: linked list
 * Return: 0 if there is a cycle 1 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *step1;
	listint_t *step2;

	if (list == NULL)
		return (0);

	step2 = list;
	step1 = list->next;

	while (step1 != NULL && step2 != NULL && step2->next != NULL)
	{
		if (step1 == step2)
			return (1);
		step1 = step1->next;
		step2 = step2->next->next;
	}
	return (0);
}
