
# :LiStackVertical:Heaps and Pri-Queue

### For more information on linked lists :LiList:
[[main-linkedlist.pdf]]

## Linked Lists
### Doubly Linked List

![[Hashtables 2024-11-15 11.28.21.excalidraw]]


## Heaps

Heaps help improve priority queues using heaps.
### 3 Famous Heaps

#### 1. Binary Heap
This tree is almost a BST. This is a **Minimum Heap**.
![[Hashtables 2024-11-15 11.31.58.excalidraw]]

The organization of the keys is such that all the holes are on the right. 
There is a sense of ordering of the keys. But not the same as a BST.
This is crucial.

This is a **Max Heap**.
![[Hashtables 2024-11-15 11.37.00.excalidraw]]

This is what a max heap is. It is essentially the "opposite" of a min (minimum) heap.

Think in terms of a tree but right the code according to an array.
![[Hashtables 2024-11-15 11.39.00.excalidraw]]

| i   | LEFT(i) | RIGHT(i) | PARENT(i) |
| --- | ------- | -------- | --------- |
| 0   |         |          |           |
| 1   |         |          |           |
| 2   |         |          |           |
| 3   |         |          |           |
| 4   |         |          |           |
| 5   |         |          |           |
| 6   |         |          |           |
| 7   |         |          |           |
| 8   |         |          |           |
| 9   |         |          |           |
Focusing on index 2 which would be 3 based on the array.
![[Hashtables 2024-11-15 11.39.00.excalidraw]]

| i   | LEFT(i) | RIGHT(i) | PARENT(i) |
| --- | ------- | -------- | --------- |
| 0   |         |          |           |
| 1   |         |          |           |
| 2   | 5       | 6        | 0         |
| 3   |         |          |           |
| 4   |         |          |           |
| 5   |         |          |           |
| 6   |         |          |           |
| 7   |         |          |           |
| 8   |         |          |           |
| 9   |         |          |           |
![[Hashtables 2024-11-15 11.39.00.excalidraw]]

Focusing on index 6. (i = 6)

| i   | LEFT(i) | RIGHT(i) | PARENT(i) |
| --- | ------- | -------- | --------- |
| 0   |         |          |           |
| 1   |         |          |           |
| 2   | 5       | 6        | 0         |
| 3   |         |          |           |
| 4   |         |          |           |
| 5   |         |          |           |
| 6   | 13      | 14       | 2         |
| 7   |         |          |           |
| 8   |         |          |           |
| 9   |         |          |           |


![[Hashtables 2024-11-15 11.39.00.excalidraw]]

Focusing on index 3 (i = 3)

| i   | LEFT(i) | RIGHT(i) | PARENT(i) |
| --- | ------- | -------- | --------- |
| 0   |         |          |           |
| 1   |         |          |           |
| 2   | 5       | 6        | 0         |
| 3   | 7       | 8        | 1         |
| 4   |         |          |           |
| 5   |         |          |           |
| 6   | 13      | 14       | 2         |
| 7   |         |          |           |
| 8   |         |          |           |
| 9   |         |          |           |
![[Hashtables 2024-11-15 11.39.00.excalidraw]]
Focusing on index 4 (i = 4)

| i   | LEFT(i) | RIGHT(i) | PARENT(i) |
| --- | ------- | -------- | --------- |
| 0   |         |          |           |
| 1   |         |          |           |
| 2   | 5       | 6        | 0         |
| 3   | 7       | 8        | 1         |
| 4   | 9       | 10       | 1         |
| 5   |         |          |           |
| 6   | 13      | 14       | 2         |
| 7   |         |          |           |
| 8   |         |          |           |
| 9   |         |          |           |
![[Hashtables 2024-11-15 11.39.00.excalidraw]]
Focusing on index 5 (i = 5)

| i   | LEFT(i) | RIGHT(i) | PARENT(i) |
| --- | ------- | -------- | --------- |
| 0   |         |          |           |
| 1   |         |          |           |
| 2   | 5       | 6        | 0         |
| 3   | 7       | 8        | 1         |
| 4   | 9       | 10       | 1         |
| 5   |         |          | 2         |
| 6   | 13      | 14       | 2         |
| 7   |         |          |           |
| 8   |         |          |           |
| 9   |         |          |           |
![[Hashtables 2024-11-15 11.46.52.excalidraw]]
Now lets try to use this as a Priority Queue
For more information.


[[main-heap.pdf]]

![[Hashtables 2024-11-15 11.49.29.excalidraw]]
Remember think in terms of tree but implementation is in terms of an array
![[Hashtables 2024-11-15 11.57.30.excalidraw]]

Runtime is equal to Height. Which is O($\log n$)

This means that assuming $n$ nodes that $O(\log n)$ (Big-O)
In fact this is actually $\Theta(\log n)$ (Big-Theta)

**HOWEVER**, there is a downside with a particular operation sometimes called a Merge.
The problem with this data structure is you cannot merge heaps quickly. But the Fibonacci heap was created for merging heaps extremely fast.
##### Insert To heap
![[Hashtables 2024-11-15 12.04.20.excalidraw]]



#### 2. Binomial Heap
#### 3. Fibonacci Heap