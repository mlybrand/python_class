class A():
    def amethod(self): print("A")

class B(A):
    pass

class C():
#class C(A):
    def amethod(self): print("C")

class D(B, C):
    pass

instance = D()
instance.amethod()
print(D.__mro__)
