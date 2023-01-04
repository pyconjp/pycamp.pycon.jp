# Pythonのデータ型（基本編）

```{admonition} 節サブタイトル
基本になるデータ型の紹介
```

代表的なPythonのデータ型と、便利な使い方を紹介します。

それぞれのデータ型の紹介で、「これだけは知っておくとよいよ」という機能を挙げます。

```{index} Built-in Types single: Built-in Types; int single: Built-in Types; float single: Built-in Types; str
```

## はじめに

本節では整数型（`int`）、浮動小数点型（`float`）、文字列型（`str`）を扱います。

データ型については、Pythonの公式ドキュメントも参考にしてください。

- 組み込み型 <https://docs.python.org/ja/3/library/stdtypes.html>

```{index} int single: Built-in Types; int
```

## 整数型（int）

整数を扱うには、整数型（`int`）を使います。

主な演算子には、前節で説明した四則演算（`+`、`-`、`*`、`/`）と剰余（`%`）の他に、累乗（`**`）があります（{numref}`type-int`）。

(type-int)=

```{code-block} pycon
:caption: "整数型"

>>> 2 + 2
4
>>> 3 - 8
-5
>>> 6 * 9
54
>>> 8 / 2
4.0
>>> 5 % 2
1
>>> 5 ** 2
25
```

割り算の結果は小数点以下も出力されます（{numref}`divide-int`）。

(divide-int)=

```{code-block} pycon
:caption: "整数型同士の商"

>>> 10 / 3
3.3333333333333335
>>> 10 / 4
2.5
>>> -10 / 4
-2.5
```

割り算の結果を整数で取得したい場合は `//` 演算子を使用します（{numref}`double-slash`）。
その場合は、小数点以下は切り捨てられます。

(double-slash)=

```{code-block} pycon
:caption: "//での割り算"

>>> 10 // 3
3
>>> 10 // 4
2
>>> -10 // 4
-3
```

```{index} float single: Built-in Types; float
```

## 浮動小数点型（float）

小数を扱うには浮動小数点型（`float`）を使います。

整数型と同様の演算子が使えます（{numref}`type-float`）。

(type-float)=

```{code-block} pycon
:caption: "浮動小数点型"

>>> 5.0
5.0
>>> 5.0 + 5.2
10.2
>>> 10.2 + 8
18.2
```

浮動小数点型と整数型との計算は浮動小数点型を返します。

```{index} str single: Built-in Types; str
```

```{index} String single: String; str
```

(types-str)=

## 文字列型（str）

文字列を使うには文字列型（`str`）を使います。

{numref}`type-str` のように、シングルクォート（`'`）かダブルクォート（`"`）の間に文字を入力します。
シングルクォート、ダブルクォートのどちらで書いても機能的な違いはありません。

(type-str)=

```{code-block} pycon
:caption: "文字列型"

>>> 'Hello,world'
'Hello,world'
>>> "Hello,world"
'Hello,world'
```

```{index} escape
```

### 文字のエスケープ

文字列中にクォート文字やその他の特殊な文字を含めたい場合は、バックスラッシュ（`\`）でエスケープします。

たとえば、シングルクォートで囲まれた文字列中では、シングルクォートを `\'` と書き、改行文字を `\n` と書きます（{numref}`escape-string`）。

(escape-string)=

```{code-block} pycon
:caption: "文字列中のエスケープ"

>>> print('I\'m Hiroki')
I'm Hiroki
>>> print('Hello\nworld')
Hello
world
```

文字列がシングルクォートを含み、ダブルクォートを含まない場合は、ダブルクォートで囲むと見やすいです（{numref}`single-quote`）。

(single-quote)=

```{code-block} pycon
:caption: "シングルクォートを含む文字列"

>>> print("I'm Hiroki")
I'm Hiroki
```

```{index} triple-quoted strings single: String; triple-quoted
```

### 三重クォート

改行を含む文字列を一度に定義するには、三重クォート（クォート文字3つ）で文字列を囲みます。

シングルクォートの場合は `'''` 、ダブルクォートの場合は `"""` です（{numref}`triple-quote`）。

(triple-quote)=

```{code-block} pycon
:caption: "三重クォート"

>>> """ foo
... bar
... baz
... """
' foo\nbar\nbaz\n'
```

```{index} concatenation single: String; concatenation
```

### 文字列の結合と繰り返し

文字列型同士を結合するには、プラス記号（`+`）を使います（{numref}`join-string`）。

アスタリスク（`*`）を使って繰り返した文字列を取得できます。

アスタリスクの左に繰り返したい文字列を、右に繰り返し回数を整数型で指定します（{numref}`multi-string`）。

(join-string)=

```{code-block} pycon
:caption: "文字列の結合"

>>> 'Mt.' + 'Fuji'
'Mt.Fuji'
```

(multi-string)=

```{code-block} pycon
:caption: "文字列の繰り返し"

>>> 'spam' * 5
'spamspamspamspamspam'
```

```{index} index single: String; index
```

### インデックス表記

文字列のある位置を指定して1文字を取り出す機能です。

(string-index)=

```{code-block} pycon
:caption: "文字列から1文字取り出し"

>>> 'python'[1]
'y'
```

文字列から1文字を取り出すには、 {numref}`string-index` のように書きます。

{numref}`string-index` では、文字列の先頭文字を0として数えた1の位置にある文字、 `'y'` が返されています。

この位置をインデックスと呼びます。インデックスには負数も使えます。 {numref}`index-image` のようになります。

(index-image)=

```{figure} images/indexing.png
:width: 400

インデックス
```

```{index} slice single: String; slice
```

### スライス

Pythonのスライスを使えば、 {numref}`slice-string` のように、2、3、4番目の文字 `'tho'` という文字列を取り出せます。

(slice-string)=

```{code-block} pycon
:caption: "文字列のスライス"

>>> 'python'[2:5]
'tho'
```

取り出す文字列の位置は、整数型を2つ、コロン（`:`）で挟んで指定します。

指定する位置は、「（取り出す文字列に）含める文字の開始位置のインデックス」から「含めずに切り捨てる文字の開始位置のインデックス」と考えられます。

{numref}`slice-string` の場合、「インデックスが2の位置の `'t'` から始まり、インデックスが5の位置の `'n'` 以降を切り捨てた」文字列、 `'tho'` が返されます。

また先頭や末尾を含む文字列のスライスは、 {numref}`slice-stirng2` のように切り出し、切り捨て位置を省略して指定します。

(slice-stirng2)=

```{code-block} pycon
:caption: "先頭末尾からのスライス"

>>> 'python'[:3]
'pyt'
>>> 'python'[4:]
'on'
```

```{index} len() single: String; len()
```

### 文字列の長さ（len()関数）

&#12288;文字列の長さを調べるには、 `len()` 関数を使います。
戻り値は整数型です（{numref}`guide-len`）。

(guide-len)=

```{code-block} pycon
:caption: "文字列長の取得"

>>> len('python')
6
```

```{index} in() single: String; in()
```

### 文字列の有無（in演算子）

文字列中にある文字列が存在するかどうかを調べるには、 `in` 演算子を使います（{numref}`guide-in`）。

(guide-in)=

```{code-block} pycon
:caption: "文字列中にある文字列が存在するかのチェック"

>>> 't' in 'python'
True
>>> 'k' in 'python'
False
>>> 'th' in 'python'
True
```

```{index} split() single: String; split()
```

### 文字列の分割（.split()メソッド）

文字列を分割するには、 `.split()` メソッドを使います。

分割したい文字列に対してメソッドを呼び出し、引数に区切り文字（デリミタ）を指定します。

ハイフンで文字列を区切るには、 {numref}`guide-split` のようにします。

(guide-split)=

```{code-block} pycon
:caption: "文字列の分割"

>>> 'pain-au-chocolat'.split('-')
['pain', 'au', 'chocolat']
```

```{index} join() single: String; join()
```

### 区切り文字による文字列の結合（.join()メソッド）

文字列を区切り文字で結合するには、 `.join()` メソッドを使います。

区切り文字に対してメソッドを呼び出し、引数に結合したい文字列のリストを指定します（{numref}`guide-join`）。

(guide-join)=

```{code-block} pycon
:caption: "文字列の結合"

>>> '-'.join(['pain', 'de', 'campagne'])
'pain-de-campagne'
```

## まとめ

代表的なPythonのデータ型と、便利な使い方を紹介しました。
型の特徴と機能を最大限に活用して開発を進めましょう。
