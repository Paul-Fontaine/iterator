from mystring import MyString
from myvector import MyVector


if __name__ == '__main__':
    my_string = MyString("Hello World !")
    my_string_iterator = my_string.get_iterator()
    my_string_iterator.show()

    # my_vector = MyVector(["Hello", "World", "!"])
    my_vector = MyVector("Hello", "World", "!")
    my_vector_iterator = my_vector.get_iterator()
    my_vector_iterator.show()
