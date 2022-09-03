a = [1, 4]


class A:
    def __init__(self, l) -> None:
        self.l = l

    def func(self, l: list):
        self.l.extend(l)


obj = A(a[:])
obj.func([3])
print(a)
