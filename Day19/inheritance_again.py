class A:
    def intro(self):
        print("A is Printing")


class B(A):
    def me(self):
        print("B is Printing")


class C(B):
    def hi(self):
        print("C is Printing")


a = A()
b = B()
c = C()



c.intro()               #even though intro is a method of class A, it can now be access by class C due to multi-level inheritance
