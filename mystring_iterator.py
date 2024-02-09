from iterator import Iterator
from overrides import override


class MyStringIterator(Iterator):
    def __init__(self, value: str):
        Iterator.__init__(self)
        self.value = value

    @override
    def has_next(self) -> bool:
        if self._position >= len(self.value) - 1:
            return False
        return True

    def get_current(self) -> str:
        return self.value[self._position]

    def show(self):
        if len(self.value) == 0:
            print('nothing to show')
            return

        while self.has_next():
            char = self.get_current()
            print(char, end=', ')
            self.next()
        print(self.get_current())
