from heap import Heap


class MinHeap(Heap):
    def _heapsort(self, index):
        stop = False
        while (index // 2 > 0) and stop == False:
            if self.heaplist[index - 1] < self.heaplist[(index - 1) // 2]:
                self.heaplist[index - 1], self.heaplist[(index - 1) // 2] = (
                    self.heaplist[(index - 1) // 2],
                    self.heaplist[index - 1],
                )
            else:
                stop = True
            index //= 2

    def insert(self, data):
        self.heaplist.append(data)
        self.size += 1
        self._heapsort(self.size)

    def pop_min(self):
        _, *self.heaplist = self.heaplist
        self.size -= 1

    def min_child(self):
        return self.heaplist[0]


n = MinHeap()
n.insert(8)
n.insert(1)
n.insert(9)
n.insert(0)
n.insert(4)
print(n.heaplist)
n.pop_min()
print(n.heaplist)

# fonte: https://www.educative.io/answers/heap-implementation-in-python
# os -1 nos index é porque no exemplo a heaplist nao começa vazia
