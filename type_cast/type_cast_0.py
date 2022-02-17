# file name: type_cast_0.py
class A:
    a = 'a'


class B(A):
    b = 'b'


class DoSomethingWithA:
    _class = A

    def do(self) -> A:
        return self._class()


class DoSomethingWithB(DoSomethingWithA):
    _class = B
