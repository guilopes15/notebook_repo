from heap import Heap


class MaxHeap(Heap):
    def _heapsort(self):
        self._build_max_heap()
        for index in range(len(self.heaplist) - 1, 0, -1):
            self.heaplist[0], self.heaplist[index] = (
                self.heaplist[index],
                self.heaplist[0],
            )
            self._max_heapify(0)

    def _build_max_heap(self):
        for index in range(len(self.heaplist) // 2 - 1, -1, -1):
            self._max_heapify(index)

    def _max_heapify(self, index):
        left = 1 + index
        right = (1 + index) + 1
        max_value = index
        heapsize = len(self.heaplist)

        if left < heapsize and self.heaplist[left] > self.heaplist[max_value]:
            max_value = left

        if (
            right < heapsize
            and self.heaplist[right] > self.heaplist[max_value]
        ):
            max_value = right

        if max_value != index:
            self.heaplist[index], self.heaplist[max_value] = (
                self.heaplist[max_value],
                self.heaplist[index],
            )
            self._max_heapify(max_value)

    def insert(self, data):
        self.heaplist.append(data)
        self.size += 1
        self._heapsort()

    def pop_max(self):
        _, *self.heaplist = self.heaplist
        self.size -= 1

    def max_child(self):
        return self.heaplist[0]


n = MaxHeap()
print(n.heaplist)
n.insert(0)
n.insert(8)
n.insert(12)
n.insert(1)
n.insert(9)
n.insert(2)
n.insert(10)

print(n.heaplist)
n.pop_max()
print(n.heaplist)


# Implementação simplificada do heapsort
# class MaxHeap(Heap):
#    def _heapsort(self, index):
#        stop = False
#        while (index // 2 > 0) and stop == False:
#            if self.heaplist[index - 1] > self.heaplist[(index - 1) // 2]:
#                self.heaplist[index - 1], self.heaplist[(index - 1) // 2] = (
#                    self.heaplist[(index - 1) // 2],
#                    self.heaplist[index - 1],
#                )
#            else:
#                stop = True
#            index //= 2
#    def insert(self, data):
#        self.heaplist.append(data)
#        self.size += 1
#        self._heapsort()
#
#    def pop_max(self):
#        _, *self.heaplist = self.heaplist
#        self.size -= 1
#
#    def max_child(self):
#        return self.heaplist[0]

# fonte: https://www.youtube.com/watch?v=WThO-rpLnks&list=PL0Z-gyL9saMdfiQfnBcaZj5VUe_HSOn2b&index=10&ab_channel=AulasdeComputa%C3%A7%C3%A3o
