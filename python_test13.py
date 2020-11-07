## 13例外処理
### 13.1 try,except,finally

def exception_test(value_1, value_2):
    print("====計算開始====")
    result = 0
    try:
        result = value_2 + value_1
    except:
        print("計算できませんでした")
        raise
    finally:
        print("計算終了")
    
    return result

#print(exception_test(100,200))
#print(exception_test(100,"200"))

### 13.2 raise
"""
try:
    print(exception_test(200,200))
    print(exception_test(300,"300"))
except:
    print("エラーを受け取りました")
    
"""
### 13.3 エラー内容の取得
import sys
import traceback

vlm = "-"*20
try:
    print(exception_test(100,"200"))
except:
    print(vlm)
    print(traceback.format_exc(sys.exc_info()[2]))
    print(vlm)
