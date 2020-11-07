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

## 4.3 ディクショナリ
### 4.3.1　ディクショナリの基本
test_dict_1 = {"YEAR":"2020","MONTH":"1","DAY":"20"}
print(test_dict_1)
print(ast)
for i in test_dict_1:
    print(i)
    print(test_dict_1[i])
    print(lvm)

### 4.3.2 valueの取得
test_dict_1 = {"YEAR":"2020","MONTH":"1","DAY":"20"}
print(test_dict_1)
print(ast)
print(test_dict_1["YEAR"])
print(lvm)
print(test_dict_1.get("YEAR"))
print(test_dict_1.get("YEARS"))
print(lvm)
print(test_dict_1.get("YEAR","NOT FOUND"))
print(test_dict_1.get("YEAES","NOT FOUND"))

### 4.3.3 要素の追加
test_dict_1 = {}
print(test_dict_1)
print(ast)
test_dict_1["YEAR"] = "2020"
test_dict_1["MONTH"] = "1"
test_dict_1["DAY"] = "20"
test_dict_1["hour"] = "24"
print(test_dict_1)

### 4.3.4 要素の削除
test_dict_1 = {"YEAR":"2020","MONTH":"1","DAY":"20"}
print(test_dict_1)
print(ast)
del test_dict_1["DAY"]
print(test_dict_1)

### 4.3.5 keyやvalueだけ取得する
test_dict_1 = {"YEAR":"2020","MONTH":"1","DAY":"1"}
print(test_dict_1)
print(ast)
print(test_dict_1.keys())
print(test_dict_1.values())

### 4.3.6 keyとvalueを同時に取得する
test_dict_1 = {"YEAR":"2020","MONTH":"1","DAY":"20"}
print(test_dict_1)
print(ast)
print("YEAR" in test_dict_1)
print("YEAES" in test_dict_1)

##4.4 セット
### 4.4.1 セットの基本
test_set_1 = {"python","-","izm",".","com","python","izm"}
print(test_set_1)
print(lvm)
for i in test_set_1:
    print(i)

test_dict_1 = {}
test_set_1 = {"python"}
print(test_set_1)
empty_set = set()
print(empty_set)
print(lvm)
### 4.4.2 要素の追加
test_set_1 = set()
test_set_1.add("python")
print(test_set_1)
test_set_1.update({"-","izm",".","com"})
print(test_set_1)

### 4.4.3 要素の削除
test_set_1 = {"python","izm",".","com"}
test_set_1.remove("izm")
test_set_1.discard(".")
print(test_set_1)

#### 4.4.4 frozeset
test_set_1 = frozenset({"python","-","izm",".","com"})
#test_set_1.remove("-")
#test_set_1.discard(".")
print(test_set_1)

print(lvm)
##4.5 スライス
### 4.5.1 スライスの基本
test_list = ["https","www","python","izm","com"]
print(test_list[:])
print(test_list[::])

### 4.5.2 要素の取得
test_list = ["http","www","python","izm","com"]
print(test_list[:4])
print(test_list[2:])
print(test_list[::2])
print(test_list[3:5])
print(test_list[-1:])
print(test_list[:-1])
print(test_list[::-1])
print(test_list[:999])
test_list[1:3] = ("WWW","PYTHON")
print(test_list)