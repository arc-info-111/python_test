## print("Hello,World")

"""
配列・連想配列

+ タプル
	任意の数の要素を持つことができる。要素の追加削除ができない。
+ リスト
	任意の数の要素を持つことができる。要素の追加削除ができる。
+ ディクショナリー
	任意の数の要素を持つことができる。keyとvalueのペア。要素の追加削除はできるが同じkeyは持てない
+ セット
	任意の数の要素を持つことができる。要素の追加削除ができるが、重複した要素を持てない。


"""


## タプル
import datetime 

def get_today(): # 要素の変更ができないため複数の値を返す関数の戻り値に適している
	today = datetime.datetime.today()
	value = (today.year, today.month, today.day) # ３要素を保持している

	return value


test_tuple = get_today()

print(test_tuple)
print(test_tuple[0])##[]にインデックス値でアクセス
print(test_tuple[1])
print(test_tuple[2])