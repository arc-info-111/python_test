## 1.1 文字列出力
print('python-izm')
print("python-izm")

## 1.2 複数行にわたって変数内容の記述を行う
test_str = """
test_1
test_2
"""
print(test_str)

## 1.3 文字列の連結
test_str1_3 = "python"
test_str1_3 = test_str1_3 + "-"
test_str1_3 = test_str1_3 + "izm"
print(test_str1_3)

## 1.4 +=を用いることによる文字列追加
test_str1_4 = "012"
test_str1_4 += "345"
test_str1_4 += "678"
test_str1_4 += "9"
print(test_str1_4)

## 1.5 *を用いて指定回数繰り返す
test_str1_5 = "012" * 3
print(test_str1_5)

## 1.6 文字列への変換 str()
test_integer = 100
print(str(test_integer)+ "円")

## 1.7 文字列の置換 "対象ファイル".replace(,)
test_str1_7 = "python-izm"
print(test_str1_7.replace("izm", "ism"))

## 1.8 文字列の分割 "対象ファイル".split()
test_str1_8 = "python-izm"
print(test_str1_8.split('-'))

## 1.9　文字列の桁揃え r(左)に文字を入力して桁揃え "対象ファイル".rjust()
test_str1_9 = '1234'
print(test_str1_9.rjust(10,"0"))
print(test_str1_9.rjust(10,"!"))
print(test_str1_9.zfill(10))
print(test_str1_9.zfill(3))

## 1.10.1 文字列の検索 先頭が任意の文字かどうか調べる
test_str1_10_1 = "python-izm"
print(test_str1_10_1.startswith("python"))
print(test_str1_10_1.startswith("izm"))

## 1.10.2 文字列の検索　任意の文字が含まれるかを調べる
test_str1_10_2 = "python-izm"
print("z" in test_str1_10_2)
print("s" in test_str1_10_2)

## 1.11 大文字・小文字変換
test_str1_11 = "Python-Izm.Com"
print(test_str1_11.upper())
print(test_str1_11.lower())

## 1.12 先頭・末尾の削除 空白を取り除く
ast = '*' * 20
print(ast)
test_str1_12 = '    python-izm.com'
print(test_str1_12)
test_str1_12 = test_str1_12.lstrip()
print(test_str1_12)
test_str1_12 = test_str1_12.lstrip("python")
print(ast)

test_str1_12 = "python-izm.com  "
print(test_str1_12+"/")
test_str1_12 = test_str1_12.rstrip()
print(test_str1_12 + "/")
test_str1_12 = test_str1_12.rstrip("com")
print(test_str1_12)

## まとめ

master = "This_"
master2 = "is_"
master3 = "test"
print(master)
master += master2
master += master3
print(master)
print(master.upper())
print(master.lower())
print(ast)
print("master" in master)
print("test" in master)
