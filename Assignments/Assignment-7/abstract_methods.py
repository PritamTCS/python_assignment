from abc import ABC , abstractmethod

class AbstractClassEx(ABC):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass

class Concrete(AbstractClassEx):
    def foo(self):
        print("In function foo")

    def bar(self):
        print("In function bar")

c = Concrete()
c.foo()

