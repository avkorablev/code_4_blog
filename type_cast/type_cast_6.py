# file name: type_cast_6.py
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
