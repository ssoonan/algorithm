#include <stdio.h>

void swap(int *p1, int *p2)
{
  int temp;
  temp = *p1;
  *p1 = *p2;
  *p2 = temp;
}

int partition(int arr[], int low, int high)
{
  // choose the pivot
  int pivot = arr[high];

  int left = low;

  for (int right = low+1; right < high; right++)
  {
    // If current element is smaller than the pivot
    if (arr[right] < pivot)
    {
      swap(&arr[left], &arr[right]);
      left++;
    }
  }
  swap(&arr[left], &arr[high]);
  return left;
}

// The Quicksort function Implement

void quickSort(int arr[], int low, int high)
{
  // when low is less than high
  if (low < high)
  {
    // pi is the partition return index of pivot

    int pi = partition(arr, low, high);

    // Recursion Call
    // smaller element than pivot goes left and
    // higher element goes right
    quickSort(arr, low, pi - 1);
    quickSort(arr, pi + 1, high);
  }
}

int main()
{
  int arr[] = {11, 7, 8, 9, 1, 5};
  int n = sizeof(arr) / sizeof(arr[0]);

  // Function call
  quickSort(arr, 0, n - 1);

  // Print the sorted array
  printf("Sorted Array\n");
  for (int i = 0; i < n; i++)
  {
    printf("%d ", arr[i]);
  }
  return 0;
}
