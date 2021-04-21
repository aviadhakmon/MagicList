class Person:
    age: int = 1


class MagicList(object):
    def __init__(self, cls_type=None):
        self.cls_type = cls_type
        self.data = list()

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        if key == len(self.data):
            self.data.append(value)
        else:
            raise IndexError("IndexError: list index out of range")

    def __str__(self):
        if self.cls_type is None:
            return str(self.data)


if __name__ == '__main__':
    try:
        a = MagicList()
        a[0] = 5
        a[1] = 1
        print(a[1])
        print(a)

    except Exception as ex:
        print(ex)
