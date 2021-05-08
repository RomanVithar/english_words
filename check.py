numb = 0

def f():
    global numb
    numb = 10


def f2():
    print(numb)
f()
f2()