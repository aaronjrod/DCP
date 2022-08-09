class SingletonMeta(type):
    # All singleton methods go in the metaclass
    def get_instance(cls):
        if cls.count == 0:
            cls.count = 1
            return cls.instance1
        cls.count = 0
        return cls.instance2

class SingletonInstance():
    def __init__(self, val) -> None:
        self.val = val
    
    def __repr__(self) -> str:
        return str(self.val)

class Singleton(metaclass=SingletonMeta):
    # Just put initialization code directly into the class
    count = 0
    instance1 = SingletonInstance(1)
    instance2 = SingletonInstance(2)

for i in range(10):
    print(Singleton.get_instance())