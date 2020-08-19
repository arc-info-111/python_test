# python_test
Python's test repository
https://www.python-izm.com/
# progress
- [x] 文字列
- [ ] 配列

## 配列
### タプル
要素の追加削除ができない
()で要素を囲む

### リスト
要素の追加削除が可能
[]で要素を囲む
+ 変数.append(引数)
  先頭の空の要素から追加する

+ 変数.insert(引数,引数)
  第一引数で追加インデックス値を、第二引数で追加要素を指定
 
+ 変数.remove(引数) 
  引数に該当する最初に該当した要素を削除
  
+ 変数.pop(引数)
  引数のインデックス値の値を取り出す（戻り値として返す）。引数なしだと要素の末尾を取り出す
  
+ 変数.index(引数)
  引数に該当するインデックス値を取得。remoceと同様に最初に該当したインデックス値を取得

### ディクショナリ
keyとvalueのセット
{}で要素を囲む
+ 変数.get(第一引数,第二引数)
	引数でkeyを指定し、要素を取得。keyがない場合、noneと表示
	第二引数を入れた場合、noneの表示を変更できる
+ 変数[key] = "要素"
	keyを指定し、要素の追加を行う

+ del 変数[key]
	引数に削除するkeyを指定

+ 変数.keys() もしくは 変数.values()
	keyもしくはvalueを取得

+ for key, value in 変数.items(): print(key,value)
	keyとvalueを同時取得

+ key in 変数
	指定したkeyを取得しているかを確認(T/F)

