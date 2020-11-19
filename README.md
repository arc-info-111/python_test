# python_test
Python's test repository
引用サイト:[python-izm](https://www.python-izm.com)

[TOC]



# 基礎編

- [x] 文字列

- [x] 数値

- [x] 日付・時間

- [x] 配列・連想配列

- [x] タプル

- [x] リスト

- [x] ディクショナリ 

- [x] セット

- [x] スライス

- [x] コメントアウト

- [x] インポート

- [x] コマンドライン引数

- [x] エスケープシーケンス

- [x] パスの結合・連結

- [x] if文

- [x] for文

- [x] while文

- [x] break

- [x] continue

- [x] rangeとxrange

- [x] print

- [x] 例外処理


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



# 応用編



- [x] 関数・メソッド
- [x] 可変長引数
- [x] クラス作成
- [x] クラス継承
- [ ] 新旧クラススタイル
- [ ] 親クラスのメソッド呼び出し
- [ ] メソッドの種類
- [ ] インスタンスメソッド
- [ ] クラスメソッド
- [ ] スタティックメソッド
- [ ] モジュールのパッケージ化
- [ ] lambda式
- [ ] ジェネレータ
- [ ] ファイル読み書き
- [ ] ファイルシステム操作
- [ ] with文
- [ ] コンテキストマネージャ
- [ ] プロパティ
- [ ] 設定ファイル
- [ ] リストのソート
- [ ] リストの逆順
- [ ] インデックスつきループ
- [ ] 要素を区切り文字で連結
- [ ] 複数のリストを同時に処理
- [ ] 要素の一括審議判定
- [ ] 順序保持ディクショナリ(2.7~3.6)
- [ ] セットの比較・作成・更新
- [ ] 内包表記
- [ ] 変数の型チェック
- [ ] 属性の有無チェック
- [ ] 呼び出し可能チェック
- [ ] 最小値・最大値の取得
- [ ] 合計値の取得
- [ ] モジュールの属性取得
- [ ] セパレータの取得
- [ ] ファイル拡張子の取得
- [ ] 改行コードの取得
- [ ] 環境変数の取得
- [ ] 乱数値の取得
- [ ] zip圧縮
- [ ] csvファイルの読み書き
- [ ] ハッシュ化
- [ ] UUID生成
- [ ] メール送信
- [ ] HTML解析
- [ ] XML解析
- [ ] JSON変換
- [ ] マルチスレッド
- [ ] XML-RPC

## format関数

文字列内に変数を埋め込むことができる

利点としては、文字列ないで動的に変わる変数を利用することができる。

```python
"任意の文字列{}任意の文字列".format(変数)
```

記述例)

```python
val1 = コーヒー
val2 = ミルク
val3 = 紅茶
print("{0}では{1}と{2}と{3}を注文した".format("カフェ",val1,val2,val3))
```



## クラス作成

classと記述し、後にクラス名が続く。

```python
class TestClass:
	
	def __init__(self, code, name):
		self.code = code
		self.name = name
		
classes = []
classes.append(TestClass(1, "テスト1"))
classes.append(TestClass(2, "テスト2"))

for test_cls in classes:
	print("====== Class ====")
	print("code -->" + str(test_cls.code))
	print("name -->" + test_cls.name)
```

3行目にある__init__というメソッドは、クラスの初期化時に必ず実行されるメソッドである。

クラスを利用する上で前準備のような処理を記述することが多い。また__init__メソッドの第一引数にselfがあるが、これはクラスのインスタンス自身を表すものでself.xxといった形で自身が保有する情報へアクセスすることができる。（省略できない）

4行目と5行目にはcodeとnameの2つのインスタンス変数を__init__メソッドの引数から自身のインスタンス(self.xxx)へ引き渡している。これによりTestClassインスタンス自身からはself.codeやself.nameでアクセスすることができ、クラスを作成した側からはインスタンス名.codeやインスタンス名.nameでアクセスすることができるようになる。

9行目、10行目でクラスのインスタンス化を行っている。クラス定義から2つのインスタンスを作成し、それぞれ別のcodeとnameを__init__メソッドを通して情報を保持させる。これによりインスタンスごとに異なる情報を設定することができるようになる。

## クラスの継承

親クラスであるCountryを定義し、country_name属性を保持する。さらにCityをCountyrクラスを継承して定義しcity_name属性を保持する。

```python
class Country:
  def __init__(self, country_name):
  	self.country_name = country_name

class City(Country):
  def __init__(self, country_name, city_name):
    super().__init__(country_name)
    self.city_name = city_name

    
classes = []
classes.append(City("Japan", "Tokyo"))
classes.append(City("USA", "Washington, D.C"))

for test_cls in classes:
  print("==== Class =====")
  print("country_name --> "+ test_cls.country_name)
  print("city_name --> "+ test_cls.city_name)
```

既存クラスの継承を行って新たにクラスを定義する場合、クラスの後に()を用いてスーパークラス名を記述する。

また親クラスが持つメソッドと同じ名前のメソッドを定義することができ、その処理内容を上書きすることができる。

例示のコードの場合、10行目で親クラスの同名メソッドを呼び出すことにより親が行っている処理をそのまま利用しつつ、小クラス側で独自の処理を追加指定していく。

小クラス側ではcountry_name属性に対して値を代入していないにもかかわらずprintで出力できているのも、親クラス側でその処理を行なっているからである。