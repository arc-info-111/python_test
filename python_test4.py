##配列・連想配列
import datetime
lvm = "-"*20
ast = "*"*20
#4.1 タプル
def get_today():
    today = datetime.datetime.today()
    value = (today.year, today.month, today.day)
    
    return value
    
test_tuple = get_today()

print(test_tuple)
print(test_tuple[0])
print(test_tuple[1])
print(test_tuple[2])

##4.2 リスト
test_list_1 = ["python","-","izm",".","com"]
print(test_list_1)
print(lvm)
for i in test_list_1:
    print(i)
##4.2.2 要素の追加
test_list_1 = []
print(test_list_1)
print(lvm)
test_list_1.append("python")
test_list_1.append("-")
test_list_1.append("izm")
test_list_1.append(".")
test_list_1.append("com")
print(test_list_1)

##4.2.3 インデックスを指定して追加
test_list_1=["python","izm","com"]
print(test_list_1)
print(lvm)
test_list_1.insert(1,"-")
test_list_1.insert(3,".")
test_list_1.insert(0,"http://www.")
print(test_list_1)
###4.2.4 要素の削除
test_list_1 =["1","2","3","2","1"]
print(test_list_1)
print(lvm)
test_list_1.remove("2")
print(test_list_1)

##4.2.5 要素の削除２
test_list_1 = ["1","2","3","2","1"]
print(test_list_1)
print(lvm)
print(test_list_1.pop(1))
print(test_list_1)
print(test_list_1.pop())
print(test_list_1)

###4.2.6 要素のインデックスを取得
test_list_1 = ["100","200","300","200","100"]
print(test_list_1.index("200"))

## 4.2.7 リスト内での要素を取得
print(test_list_1.count("200"))
