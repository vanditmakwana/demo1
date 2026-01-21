a="globle"
def instance():
    b="outer"
    def inner():
        c="inner"
        print(c)
    inner()
    print(b)
instance()
print(a)