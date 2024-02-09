from mystring_iterator import MyStringIterator


class MyString(str):
    def __new__(cls, string: str):
        return str.__new__(cls, string)

    def get_iterator(self) -> MyStringIterator:
        return MyStringIterator(self)
