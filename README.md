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

- [ ] print

- [ ] 例外処理

  

- [ ] 

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



- [ ] 関数・メソッド
- [ ] 可変長引数
- [ ] クラス作成
- [ ] クラス継承
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

