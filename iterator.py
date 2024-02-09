from abc import ABC, abstractmethod


class Iterator(ABC):
    def __init__(self):
        self._position = 0

    @abstractmethod
    def has_next(self) -> bool:
        raise NotImplementedError

    def next(self):
        self._position += 1
