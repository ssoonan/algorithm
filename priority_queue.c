#include <stdio.h>
#include <stdlib.h>

// 힙 구조 정의
typedef struct
{
  int *data;    // 힙 데이터 배열
  int size;     // 현재 힙 크기
  int capacity; // 힙의 최대 용량
} Heap;

// 힙 생성 함수
Heap *createHeap(int capacity)
{
  Heap *heap = (Heap *)malloc(sizeof(Heap));
  heap->data = (int *)malloc(capacity * sizeof(int));
  heap->size = 0;
  heap->capacity = capacity;
  return heap;
}

void swap(int *a, int *b)
{
  int tmp = *a;
  *a = *b;
  *b = tmp;
}

// 힙 삽입(Heapify Up)
void heapifyUp(Heap *heap, int index)
{
  if (index && heap->data[index] > heap->data[(index - 1) / 2])
  {
    // 부모와 자식 교환
    swap(&heap->data[index], &heap->data[(index - 1) / 2]);
    // 재귀 호출로 부모까지 검사
    heapifyUp(heap, (index - 1) / 2);
  }
}

// 요소 삽입 함수
void insert(Heap *heap, int value)
{
  if (heap->size == heap->capacity)
  {
    printf("Heap is full!\n");
    return;
  }
  // 새로운 요소 삽입 후 Heapify Up 수행
  heap->data[heap->size] = value;
  heapifyUp(heap, heap->size);
  heap->size++;
}

// 힙 삭제(Heapify Down)
void heapifyDown(Heap *heap, int index)
{
  int largest = index;
  int left = 2 * index + 1;
  int right = 2 * index + 2;

  if (left < heap->size && heap->data[left] > heap->data[largest])
    largest = left;
  if (right < heap->size && heap->data[right] > heap->data[largest])
    largest = right;
  if (largest != index)
  {
    // 부모와 자식 교환
    int temp = heap->data[index];
    heap->data[index] = heap->data[largest];
    heap->data[largest] = temp;
    // 자식까지 Heapify Down 수행
    heapifyDown(heap, largest);
  }
}

// 최대값 삭제 함수
int extractMax(Heap *heap)
{
  if (heap->size <= 0)
    return -1; // 힙이 비어있음
  int max = heap->data[0];
  heap->data[0] = heap->data[--heap->size];
  heapifyDown(heap, 0);
  return max;
}

int main()
{
  Heap *heap = createHeap(10);
  insert(heap, 20);
  insert(heap, 15);
  insert(heap, 30);
  insert(heap, 10);
  insert(heap, 40);

  printf("Max: %d\n", extractMax(heap)); // 출력: Max: 30
  printf("Max: %d\n", extractMax(heap)); // 출력: Max: 20
  printf("Max: %d\n", extractMax(heap));

  free(heap->data);
  free(heap);
  return 0;
}
