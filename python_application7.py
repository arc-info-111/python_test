### 7.1 モジュールのパッケージ化
"""
import sys

sys.path.append("/Users/M.A")

import Desktop.python_test.calc
print(Desktop.python_test.calc.plus_value(1, 1))

"""
### 7.2 lambda式
#名前のない関数の作成

def plus_value(num_1, num_2):
    return num_1 + num_2
    
print(plus_value(10, 100))

l_func = lambda num_1, num_2: num_1 + num_2
print(l_func(10, 100))

### 7.3 ジェネレータ
#メモリを効率的に確保する
def func_sample():
    yield("おはよう")
    yield("こんにちは")
    yield("こんばんは")
 

#for i in func_sample():
#    print(i)

f = func_sample()
print(next(f))
print(next(f))
#print(f.next())

gen_sample = (i for i in "おはよう　こんにちは　こんばんは".split())

print(gen_sample)
for i in gen_sample:
    print(i)
