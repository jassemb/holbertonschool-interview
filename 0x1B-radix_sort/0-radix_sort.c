#include "sort.h"
/**
 * getMax - function to get maximum value in arr
 * @array: arry to be sorted.
 * @n: size of array
 * Return: max
 */
int getMax(int *array, int n)
{
	int mx = array[0];
	int i;

	for (i = 1; i < n; i++)
		if (array[i] > mx)
			mx = array[i];
	return (mx);
}
/**
 * countSort - to do counting sort of arr
 * @array: arry to be sorted.
 * @n: size of array
 * @exp: expectued number
 */
void countSort(int *array, int n, int exp)
{
	int output[n];
	int i, count[10] = {0};

	for (i = 0; i < n; i++)
		count[(array[i] / exp) % 10]++;

	for (i = 1; i < 10; i++)
		count[i] += count[i - 1];

	for (i = n - 1; i >= 0; i--)
	{
		output[count[(array[i] / exp) % 10] - 1] = array[i];
		count[(array[i] / exp) % 10]--;
	}
	for (i = 0; i < n; i++)
		array[i] = output[i];
}
/**
 * radix_sort - function that sorts an array of integers in ascending order
 * @array: arry to be sorted.
 * @size: size of array
 */
void radix_sort(int *array, size_t size)
{
	int exp;
	int m = getMax(array, size);
	if (!array || size < 2)
		return;

	for (exp = 1; m / exp > 0; exp *= 10)
	{
		countSort(array, size, exp);
		print_array(array, size);
		printf("\n");
	}
	
}
