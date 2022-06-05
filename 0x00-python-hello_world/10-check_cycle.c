#include "lists.h"
/**
 * check_cycle -  checks if a singly linked list has a cycle in it.
 * @list: is the linked list
 * return: 0 if it does not have cycle in it. 1 in otherwise
 */
int check_cycle(listint_t *list)
{
	int cycle = 0;
	listint_t *tortoise = NULL, *hare = NULL;

	if (!list)
		return (cycle);

	tortoise = list, hare = tortoise->next;
	while (hare && hare->next && hare->next->next)
	{
		if (tortoise == hare)
			return (1);
		tortoise = tortoise->next;
		hare = hare->next->next;
	}
	return (cycle);
}
