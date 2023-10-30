import math

# heap 即堆，根据性质可以分为大根堆和小根堆，存储形式是一棵完全二叉树，因此使用数组来保存。如果是大根堆，那么父节点大于等于子节点，根节点是最大的。如果是小根堆，那么父节点小于等于子节点，根节点是最小的。
class MinHeap:

    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0


    def perc_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
            i = i // 2

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size += 1
        self.perc_up(self.current_size)

    def perc_down(self, i):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = tmp
            i = mc

    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i*2] < self.heap_list[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def del_min(self):
        ret = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.perc_down(1)
        return ret
    
import random
    
min_heap = MinHeap()

# 随机插入10个元素 
for i in range(10):
    min_heap.insert(random.randint(1, 100))

# 检查最小元素  
print(min_heap.heap_list[1]) 

# 删除最小元素
print(min_heap.del_min())
print(min_heap.heap_list[1])

# 再插入一个较小元素 
min_heap.insert(0)
print(min_heap.heap_list[1])