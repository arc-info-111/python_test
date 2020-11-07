# 12　print
## 12.1 基本的な使い方
print("python")
print("-")
print("izm")
print("com")

## 12.2 改行しない
print("python", end=" ")
print("-", end=" ")
print("izm", end=" ")
print("com")

## 12.3 出力先の変更

f_obj = open("text.txt", "w")
print("pyton-izm.com", file=f_obj)

## 12.4 フォーマット出力
print("Pythonの学習サイト：%s" % "python-izm.com")
print("Pythonの学習サイト：%s-%s-%s" % ("python","izm","com"))

test_int = 100+100
test_str = "python-izm.com"
print("サイト開設 %d日目 %s" % (test_int,test_str))


print("Pythonの学習サイト：{}".format("python-izm.com"))
print("Pythonの学習サイト：{0}-{1}-{2}".format("python","izm","com"))
print("サイト開設 {1}日目 {0}".format(test_str,test_int))

