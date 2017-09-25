class Singletone:
    instanse = None

    def __new__(cls, *args, **kwargs):
        if Singletone.instanse is None:
            Singletone.instanse = object.__new__(cls)
        return Singletone.instanse

    def __init__(self, a):
        self.a = a


a1 = Singletone(10)
a2 = Singletone(20)
print(a1.a)
print(a2.a)
print(a1 is a2)
print(id(a1), id(a2))
