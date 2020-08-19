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
"""
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

"""
##  リスト
"""
test_list_1 = ["python", "-", "izm", ".", "com"]# タプルと異なり[]で囲む
print(test_list_1)

print("================================")

for i in test_list_1:
	print(i)

### リスト　空の要素への追加

test_list_2 = []
print(test_list_2)

print("==================================")

test_list_2.append("python")
test_list_2.append("-")
test_list_2.append("izm")
test_list_2.append(".")
test_list_2.append("com")

print(test_list_2)


### リスト　インデックスを指定して追加

test_list_3 = ["python", "izm", "com"]
print(test_list_3)

print("=================================")

test_list_3.insert(1, "-")# 引数はそれぞれ追加箇所のインデックス値、追加要素
test_list_3.insert(3, ".")

print(test_list_3)

test_list_3.insert(0, "http://www.")# インデックス値0で先頭への追加
print(test_list_3)

### リスト　要素の削除
test_list_4 = ["1", "2", "3", "2", "1"]
print(test_list_4)

print("================================")
test_list_4.remove("2")#　引数に該当する"一番最初"に該当した要素を削除

print(test_list_4)

### リスト　要素の削除2
test_list_5 = ["1","2","3","2","1"]
print(test_list_1)

print("================================")
print(test_list_5.pop(1))# 引数のインデックス値の要素の削除を行い、削除した値を戻り値として返す
print(test_list_5)

print(test_list_5.pop())# 引数なしだとリスト要素の末尾が削除される
print(test_list_5)


### リスト　要素のインデックスを取得
print(test_list_1)
print(test_list_1.index("python"))#指定の引数に該当するインデックス値を取得。removeと同じく最初に見つかったインデックス値のみ取得


"""
## ディクショナリ
test_dict_1 = {"YEAR":"2020", "MONTH":"1", "DAY":"20"}# {}で要素を宣言.要素をkey:valueで宣言
print(test_dict_1)

print("===============================")

for i in test_dict_1:
	print(i)
	print(test_dict_1[i])
	print("==================================")

## ディクショナリ　valueの取得
print(test_dict_1)

print("==================================")

print(test_dict_1.get("YEAR"))
print(test_dict_1.get("YEARS"))# ディクショナリ内に対応するkeyがなくともerrorにならない

print("====================================")

print(test_dict_1.get("YEAR","NOT FOUND"))# 台に引数に該当するkeyが存在しない場合のデフォルト値を設定
print(test_dict_1.get("YEARS", "NOT FOUND"))

## ディクショナリ　要素の追加

test_dict_1 = {}

print(test_dict_1)

print("================================")
test_dict_1["YEAR"] = "2020"
test_dict_1["MONTH"] = "1"
test_dict_1["DAY"] = "20"

print(test_dict_1)

## ディクショナリ　要素の削除
test_dict_1 = {"YEAR":"2020", "MONTH":"1", "DAY":"20"}
print(test_dict_1)

print("=================================")
del test_dict_1["DAY"] #引数に削除するkeyを選択
print(test_dict_1)

## ディクショナリ　keyやvalueだけを取得する
print(test_dict_1)

print("==================================")

print(test_dict_1.keys())
print(test_dict_1.values())

## ディクショナリ　keyとvalueを同時に取得する
for key, value in test_dict_1.items():
	print(key, value)

## ディクショナリ　keyを保持しているかを確認
print("==================================")
print("YEAR" in test_dict_1)
print("YEARS" in test_dict_1)

