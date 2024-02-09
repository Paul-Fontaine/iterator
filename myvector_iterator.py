from iterator import Iterator
from overrides import override
from typing import Any


class MyVectorIterator(Iterator):
    def __init__(self, my_vector: '"MyVector"'):
        Iterator.__init__(self)
        self.elements = my_vector

    @override
    def has_next(self) -> bool:
        if self._position >= len(self.elements) - 1:
            return False
        return True

    def get_current(self) -> Any:
        return self.elements[self._position]

    def show(self):
        if len(self.elements) == 0:
            print('nothing to show')
            return

        while self.has_next():
            elt = self.get_current()
            print(elt, end=', ')
            self.next()
        print(self.get_current())

