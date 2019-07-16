## * a tuple of element 
def foo(*args):
    for e in args:
        print(e)

foo(1)
foo(1,3,5)

## * a dictionary of element 
def bar(**kwargs):
    for e in kwargs:
        print(e,kwargs[e])

bar(name='andy')
bar(name='andy',age='54')

a=(1,2,3,4)
b=[1,2,3,4]
print(*a)
print(*b)

d = {'name':'andy','age':55}
bar(**d)

def lee(**any_var):
    for e in any_var:
        print(e,any_var[e])
lee(**d)

def foo_bar(*args, **kwargs):
    for e in args:
        print(e)
    for e in kwargs:
        print(e,kwargs[e])

foo_bar(3)
foo_bar(4,name='andy')
foo_bar(3,4,name='andy',age='55')
foo_bar('3')
