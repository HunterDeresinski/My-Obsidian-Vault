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