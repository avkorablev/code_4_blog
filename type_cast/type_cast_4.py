# file name: type_cast_5.py
import typing as tp


class A:
    a = 'a'


class B(A):
    b = 'b'


TV = tp.TypeVar('TV', bound=A)


class DoSomethingWithA(tp.Generic[TV]):
    _class: tp.Type[TV] = A

    def do(self) -> TV:
        return self._class()


class DoSomethingWithB(DoSomethingWithA):
    _class = B
