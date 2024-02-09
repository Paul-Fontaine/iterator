from myvector_iterator import MyVectorIterator


class MyVector(list):
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], list):
            # for MyVector([a, b, c])
            list.__init__(self, args[0])
        else:
            # for MyVector(a, b, c)
            list.__init__(self, args)

    def get_iterator(self) -> MyVectorIterator:
        return MyVectorIterator(self)
