def decorator(fun):
    def unknown():
        print("first call")
        fun()
        print("second call")
        return unknown

@decorator
def hello():
    print("hello")
hello()
