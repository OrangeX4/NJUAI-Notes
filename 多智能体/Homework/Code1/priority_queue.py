# 这里就不自己实现一个支持 update 的优先级队列了, 找了一份网上的代码
# Code from: https://github.com/denizetkar/priority-queue/blob/main/priority_queue.py

class PriorityQueue:
    def __init__(
        self,
        arr=None,
        has_higher_priority=lambda x, y: x[0] < y[0],
        id_of=lambda x: x[1],
    ):
        if arr is None:
            arr = []
        self._heap = arr
        self.has_higher_priority = has_higher_priority
        self.id_of = id_of
        self._elem_idxs = {}
        for i, elem in enumerate(self): # type: ignore
            self._add_elem_idx(elem=elem, idx=i)

        self._heapify()

    def _get_elem_idxs(self, elem=None, elem_id=None):
        if elem is not None:
            elem_id = self.id_of(elem)
        return self._elem_idxs.get(elem_id, None)
    
    def exist(self, elem=None, elem_id=None):
        return self._get_elem_idxs(elem, elem_id) != None

    def _add_elem_idx(self, idx, elem=None, elem_id=None):
        if elem is not None:
            elem_id = self.id_of(elem)
        assert self._get_elem_idxs(elem_id=elem_id) is None, "`elem` must not exist"
        self._elem_idxs[elem_id] = idx

    def _remove_elem_idx(self, elem=None, elem_id=None):
        if elem is not None:
            elem_id = self.id_of(elem)
        self._elem_idxs.pop(elem_id, None)

    def __len__(self):
        return len(self._heap)

    def __getitem__(self, i):
        return self._heap[i]

    @staticmethod
    def left_child_idx(i):
        return 2 * i + 1

    @staticmethod
    def right_child_idx(i):
        return 2 * i + 2

    @staticmethod
    def parent_idx(i):
        return (i - 1) // 2

    def _swap_elems(self, i, j):
        elem1, elem2 = self[i], self[j]
        self._heap[i], self._heap[j] = elem2, elem1
        self._remove_elem_idx(elem=elem1)
        self._add_elem_idx(elem=elem1, idx=j)
        self._remove_elem_idx(elem=elem2)
        self._add_elem_idx(elem=elem2, idx=i)

    def _bubble_up(self, i):
        while True:
            if i == 0:
                return
            parent_idx = self.parent_idx(i)
            if not self.has_higher_priority(self[i], self[parent_idx]):
                return
            self._swap_elems(parent_idx, i)
            i = parent_idx

    def _bubble_down(self, i):
        while True:
            left_child_idx = self.left_child_idx(i)
            right_child_idx = self.right_child_idx(i)
            if left_child_idx >= len(self):
                return
            prio_idx = left_child_idx
            if right_child_idx < len(self):
                if self.has_higher_priority(self[right_child_idx], self[prio_idx]):
                    prio_idx = right_child_idx

            if not self.has_higher_priority(self[prio_idx], self[i]):
                return

            self._swap_elems(i, prio_idx)
            i = prio_idx

    def _heapify(self):
        if len(self) == 0:
            return
        max_idx = self.parent_idx(len(self) - 1)
        for idx in range(max_idx, -1, -1):
            self._bubble_down(idx)

    def _append(self, elem):
        self._add_elem_idx(elem=elem, idx=len(self))
        self._heap.append(elem)

    def put(self, elem):
        self._append(elem)
        self._bubble_up(len(self) - 1)

    def _remove_last(self):
        last_idx = len(self) - 1
        elem = self._heap.pop(last_idx)
        self._remove_elem_idx(elem=elem)
        return elem

    def top(self):
        last_idx = len(self) - 1
        elem = self._heap[last_idx]
        return elem

    def pop(self):
        if len(self) == 0:
            return None
        self._swap_elems(0, len(self) - 1)
        elem = self._remove_last()
        self._bubble_down(0)
        return elem

    def update_elem(self, elem_id, new_elem):
        idx = self._get_elem_idxs(elem_id=elem_id)
        if idx is None:
            return

        elem = self._heap[idx]
        self._heap[idx] = new_elem
        self._remove_elem_idx(elem_id=elem_id)
        self._add_elem_idx(elem=new_elem, idx=idx)
        if self.has_higher_priority(new_elem, elem):
            self._bubble_up(idx)
        elif self.has_higher_priority(elem, new_elem):
            self._bubble_down(idx)

    def put_or_update(self, elem):
        elem_id = self.id_of(elem)
        idx = self._get_elem_idxs(elem_id=elem_id)
        if idx != None:
            self.update_elem(elem_id, elem)
        else:
            self.put(elem)

    def remove(self, elem_id):
        idx = self._get_elem_idxs(elem_id=elem_id)
        if idx is None:
            return None

        last_idx = len(self) - 1
        last_elem = self[last_idx]
        self._swap_elems(idx, last_idx)
        elem = self._remove_last()
        if self.has_higher_priority(last_elem, elem):
            self._bubble_up(idx)
        elif self.has_higher_priority(elem, last_elem):
            self._bubble_down(idx)

        return elem

    def __repr__(self) -> str:
        return repr(self._heap)