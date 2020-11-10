
##関数・メソッド
###1.1 関数の基礎
"""
def test_func():
    print("call test_func")
    
test_func()
"""
###1.2 引数の基礎
"""
def test_func(num_1, num_2, oprn):
    if oprn == 1:
        print("足し算開始")
        print(num_1 + num_2)
    elif oprn == 2:
        print("引き算開始")
        print(num_1 - num_2)
    elif oprn == 3:
        print("掛け算開始")
        print(num_1 * num_2)
    elif print == 4:
        print("割り算開始")
        print(num_1/num_2)
    else:
        print("不明なオペレーション指定です")
    
test_func(100, 10, 3)
"""
###1.3 引数の初期値
"""
def test_func(num_1, num_2, oprn=1):
    if oprn == 1:
        print("足し算開始")
        print(num_1 + num_2)
    elif oprn == 2:
        print("引き算開始")
        print(num_1 - num_2)
    elif oprn == 3:
        print("掛け算開始")
        print(num_1 / num_2)
    elif oprn == 4:
        print("割り算開始")
        print(num_1 / num_2)
    else:
        print("不明なオペレーションです")
    
test_func(100,10,4)
"""
###1.4 関数とメソッド
# 関数
def test_func():
    print("call test_func")

class Test_Class:
    def test_method():
        print("call test_method")
        
lvm = "-"*20
print(lvm)
print(test_func)
print(Test_Class.test_method)

print(lvm)
print(type(test_func))
print(type(Test_Class.test_method))

print(lvm)
t = Test_Class()
print(test_func)
print(t.test_method)
