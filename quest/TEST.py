class SomeClass(object):
    # def __new__(cls):
    #     print("new")
    #     return super(SomeClass, cls).__new__(cls)

    def some(self):
        print("init")

obj = SomeClass()
obj.some()