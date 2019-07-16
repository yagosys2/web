class A(object):
    def foo(self, x):
        print "executing foo(%s, %s)" % (self, x)

    @classmethod
    def class_foo(cls, x):
        print "executing class_foo(%s, %s)" % (cls, x)

    @staticmethod
    def static_foo(x):
        print "executing static_foo(%s)" % x    

a = A()
## a.foo(1) 是个对象方法
## a.class_foo(1) 是个类方法，默认implicit绑定到类 With classmethods, the class of the object instance is implicitly passed as the first argument instead of self
## a.static_foo(1) 是个类方法，同时绑定到类及对象。
##With staticmethods, neither self (the object instance) nor  cls (the class) is implicitly passed as the first argument. They behave like plain functions except that you can call them from an instance or the class:
