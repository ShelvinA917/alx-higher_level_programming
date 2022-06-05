#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - insert a node
 * @head: is the first node
 * @number: new value
 * return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *past = NULL, *present = *head, *new = NULL;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;

	if (!present)
		*head = new;
	else if (new->n < present->n)
	{
		*head = new;
		new->next = present;
	}
	else
	{
		while (present)
		{
			past = present;
			present = present->next;
			if (!present || new->n < present->n)
			{
				past->next = new;
				new->next = present;
				break;
			}
		}
	}
	return (new);
}
