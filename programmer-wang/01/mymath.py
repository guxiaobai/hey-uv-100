PI = 3.14

def add(a, b):
    return a + b


def add_global(name, value):
    g = globals()
    g[name] = value