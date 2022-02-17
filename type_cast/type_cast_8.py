# file name: type_cast_8.py
import typing as tp


class A:
    a = 'a'


class B(A):
    b = 'b'


TV = tp.TypeVar('TV', bound=A)


class DoSomethingWith(tp.Generic[TV]):
    _class: tp.Type[TV]

    def do(self) -> TV:
        return self._class()


class DoSomethingWithA(DoSomethingWith):
    _class = A


class DoSomethingWithB(DoSomethingWith):
    _class = B
