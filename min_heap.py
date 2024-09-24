class MinHeap:
    def __init__(self, elements=None):
        self.heap = []
        if elements:
            self.build_min_heap(elements)
    
    def parent(self, index):
        return (index - 1) >> 1
    
    def left_child(self, index):
        return (index << 1) + 1
    
    def right_child(self, index):
        return (index << 1) + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def heapify(self, index):
        left = self.left_child(index)
        right = self.right_child(index)
        smallest = index
        
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            self.swap(index, smallest)
            self.heapify(smallest)
    
    def build_min_heap(self, elements):
        self.heap = elements
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify(i)
    
    def pop(self):
        if not self.heap:
            return None
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify(0)
        return root

    def __str__(self):
        return str(self.heap)

# Example Usage
elements = [5, 13, 2, 25, 7, 17, 20, 8, 4]
min_heap = MinHeap(elements)
print("Initial Min-Heap:", min_heap)

# Pop the root
print("Pop root:", min_heap.pop())
print("Heap after popping the root:", min_heap)

# Add new element
new_element = 3
min_heap.heap.append(new_element)
min_heap.heapify(len(min_heap.heap) - 1)
print("Heap after adding new element (3):", min_heap)
