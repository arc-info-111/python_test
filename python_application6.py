## 6 メソッドの種類
class TestClass:

    # インスタンスメソッド
    def sample_instancemethod(self, arg_1):
        pass
        
    # クラスメソッド
    @classmethod
    def sample_classmethod(cls, arg_1):
        pass
        
    # スタティックメソッド
    @staticmethod
    def sample_staticmethod(arg_1, arg_2):
        pass
        
### 6.1 インスタンスメソッド
class TestClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def sample_instancemethod(self, display_x=True, display_y=True):
        if display_x:
            print("x is {}".format(self.x))
        if display_y:
            print("y is {}".format(self.y))
            
test_class_1 = TestClass(100,50)
test_class_1.sample_instancemethod(display_x=False)
test_class_1.sample_instancemethod(display_y=False)


### 6.2 クラスメソッド
import datetime

class TestClass:
    
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        
    # クラスメソッド
    @classmethod
    def sample_classmethod(cls, date_diff=0):
        today = datetime.date.today()
        d = today + datetime.timedelta(days=date_diff)
        return cls(d.year, d.month, d.day)
        
# インスタンス化しないで呼び出し
test_class_1 = TestClass.sample_classmethod()
print(test_class_1.year, test_class_1.month, test_class_1.day)

# インスタンス化しないで呼び出し
test_class_2 = TestClass.sample_classmethod(-10)
print(test_class_2.year, test_class_2.month, test_class_2.day)

# 通常のインスタンス
test_class_3 = TestClass(2000, 1, 1)
print(test_class_3.year, test_class_3.month, test_class_3.day)


### 6.3 スタティックメソッド
class TestClass:
    
    # スタティックメソッド
    @staticmethod
    def sample_staticmethod(x,y):
        return x + y

# インスタンス化しないで呼び出し
print(TestClass.sample_staticmethod(10, 100))

# インスタンス化してからでも呼び出せる
test_class = TestClass()
print(test_class.sample_staticmethod(10,100))
