(guide-intro)=

# Pythonをはじめよう

```{admonition} 節サブタイトル
実践を通したPythonの特徴と基本の紹介
```

Pythonの特徴と基本を紹介します。
ただ紹介するだけではなく、簡単なプログラムを実装しつつ実践的に学んでいきます。

(enjoy-python)=

## Pythonを楽しもう

Pythonのインストールはできましたか？

ここではPythonの基本の基本を紹介します。
Pythonインタープリタに入力し結果を確認したり、Pythonファイル(.pyファイル)を作り実行しながら、Pythonにふれあいましょう。

ここでは、「FizzBuzz」という簡単なプログラム（詳細は後述）を実装できることを目的にします。

Pythonについてより詳しくは、後述の節で説明します。
つまり、ここで説明したことのすべてをいま理解しようとしなくても大丈夫です。次節以降でおさらいをしていきます。

```{index} interpreter
```

### Pythonインタープリタ

さっそくPythonで遊んでみましょう。

ターミナル(WindowsではPowerShell)を立ち上げて `python` (macOS、Linuxの場合は `python3`)と入力し、Pythonインタープリタを対話モードで起動しましょう（{numref}`python-interpreter`）。

(python-interpreter)=

```{code-block} bash
:caption: "Pythonインタープリタの起動"

 $ python
Python 3.12.6 (main, Jun  6 2024, 18:26:44) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
 >>>
```

初めにPythonインタープリタの情報と、大なり記号3つ（`>>>`）が表示されます。

この(`>>>`)がPythonの対話モードでの入力をうながすプロンプトです。終了するには {kbd}`Ctrl`-{kbd}`D`または `quit()` を入力します（Windowsでは{kbd}`Ctrl`-{kbd}`Z`+{kbd}`Enter`）。

```{index} calculator
```

#### Pythonを電卓にする

電卓のようにPythonを使ってみましょう（{numref}`python-calc`）。

(python-calc)=

```{code-block} pycon
:caption: "四則演算と代入"

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
>>> width = 60
>>> height = 90
>>> width * height
5400
```

初めの4つは整数型（int）での四則演算（`+`、`-`、`*`、`/`）と剰余（`%`）です。

次に等号（`=`）を使って値を代入しています。

`width` (幅)、 `height` (高さ)という変数を作成し、2つを掛け合わせて面積を求めています。

**変数を作成** とは、データ(ここでは60など)にラベル(ここではwidthなど)を付けて、後で使用できるようにすることです。

```{index} str
```

### 文字列

数字だけを扱うなら卓上電卓で十分ですね。文字列型（str）を使ってみましょう。

{numref}`string-type` のように、シングルクォート（`'`）かダブルクォート（`"`）の間に文字を入力することで、文字列を定義します。

(string-type)=

```{code-block} pycon
:caption: "文字列型"

>>> 'Hello,world'
'Hello,world'
>>> "Monty Python's Flying Circus"
"Monty Python's Flying Circus"
```

文字列中にシングルクォートを含む場合はダブルクォートを使います
（ {ref}`types-str` で説明する文字のエスケープも使えます）。

文字列は順序を持つシーケンス型の1つです。

```{admonition} コラム: シーケンス型
シーケンス型は順序を持つ型で、Python標準では他にもリスト(`list`)型、タプル(`tuple`)型、レンジ(`range`)型などがあります。
シーケンス型は後ほど説明するインデックスによる取得もサポートしています。

シーケンス型の詳細はPythonの公式ドキュメントを参照してください。

- シーケンス (<https://docs.python.org/ja/3/library/stdtypes.html#typesseq>)
```

```{index} list
```

### リスト

リスト（list）は、複数のデータ型の入れ物として使えます（{numref}`list`）。

(list)=

```{code-block} pycon
:caption: "リスト"

>>> ['Hello', 3]
['Hello', 3]
```

リストも文字列と同じで、順序を持つ繰り返し可能な型(シーケンス)の1つです。

複数のデータ型と組み合わせて使えるコレクションの1つでもあります。

```{index} comment
```

### コメント

`#` より右以降の文字列は「コメント」となり、プログラムとして実行されません。

(python-comment)=

```{code-block} pycon
:caption: "コメントの書き方"

>>> # ここはコメント文
>>> a = 1  # コードの右側にも書ける
```

```{index} function
```

### 関数

関数とはプログラムの中で処理をひとまとめにしたものです。
Pythonでは関数は、 `def` を使って以下のように書きます。
末尾にはコロン（`:`）が必要です。

```none
def ＜関数名＞(＜引数の変数名＞):
```

値を返すには、 `return` を使います。引数を2つ受け取り、合計値を返す関数は {numref}`function-def` になります。

(function-def)=

```{code-block} pycon
:caption: "関数定義と呼び出し"

>>> def add(a, b):
...     return a + b
...
>>> add(1, 3)
4
```

```{index} indent
```

Python はブロック構造を **インデント** （通常は4つのスペース）で書きます。

C言語のように波括弧（`{ }`）で囲む必要はなく、インデント自体が文の構造となります。

`add()` 関数内の1行目のreturn文は関数の中身なので、インデントで字下げします。

関数を書き終わったときにも **改行を入力** してください（最後の入力が文として終了していない場合、プロンプトが3つのドット（`...`）になります）。

関数を呼び出すには関数名に括弧（`( )`）を付けて実行します。

{numref}`function-def` のように引数がある場合は、括弧内に引数を渡します。1と3を足した値、4が返されています。

```{admonition} コラム: インデントの表示
このドキュメントをWebブラウザで見ている場合、 `def` と `return` が同じレベルにあるように見える事があります。
実際には、 `return` の前に、スペース4つが挿入されて、ブロック構造を表しています。
```

```{index} Built-in Functions
```

#### 組み込み関数

Pythonには標準でいくつか関数が提供されています。これを組み込み関数と呼びます。

たとえば、指定された小数点を丸めた値を作成する `round()` 関数は、 このように使います。

```{index} pair: Built-in Functions; round();
```

```{code-block} pycon
:caption: "組み込み関数round"

>>> round(10.4)
10
```

組み込み関数の一覧は、次のドキュメントを参照してください。

- 組み込み関数 <https://docs.python.org/ja/3/library/functions.html>

```{index} FizzBuzz
```

## FizzBuzz

ここで「FizzBuzz」というゲームを解くプログラムをPythonで書いてみましょう。

FizzBuzzとは、複数の人が集まって行うゲームです。

ひとりひとりが1から順に数字を発言し、数字が3で割り切れる場合は「Fizz」、5で割り切れる場合は「Buzz」、3 と5 で割り切れる場合は「FizzBuzz」と発言するゲームです。

1から15までの答えを並べると次のようになります。

```{code-block} none
:caption: "FizzBuzzの15までの回答"

1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz
```

1から100までのFizzBuzzを表示するPythonプログラムを作りましょう。

FizzBuzzは簡単な問題ですが、実装する言語の制御文(繰り返し、条件分岐)を使いこなす必要があり、言語入門の第一歩としてちょうどよい題材です

% FizzBuzz Question/Test について書くかどうか http://blog.codinghorror.com/why-cant-programmers-program/_

### Pythonファイル

Pythonファイルを作成しFizzBuzzを実装していきましょう。

今まではPythonインタープリタの対話モード上でPythonのコードを直接実行していましたが、少し長い処理を書くには不便です。

Python インタープリタの対話モードを終了し、fizzbuzz.py というファイルを作成します。

{numref}`fizzbuzz-1` のように書きます。

(fizzbuzz-1)=

```{code-block} python
:caption: fizzbuzz.py

def fizzbuzz(num):
    return num

print(fizzbuzz(4))
```

この `fizzbuzz()` 関数はなにも処理をせず引数をそのまま返します。これから処理を追加していくので安心してください。

`print()` 関数を使っているのは実行結果を表示するためです。

対話モードでは、変数の値や関数の戻り値を変数に代入しない場合に、自動的に値を表示してくれました。

Python ファイルを作成して実行する場合は、 `print()` 関数が必要です。

`fizzbuzz.py` を実行するには、 `python` コマンドに引数として渡します（{numref}`exec-fizzbuzz`）。

(exec-fizzbuzz)=

```{code-block} bash
:caption: "fizzbuzz.pyの実行"

$ python fizzbuzz.py  # macOS、Linuxの場合はpython3（以下同様）
4
```

ファイルが存在するフォルダと、ターミナル/PowerShellの現在位置があっているか注意してください。
fizzbuzz.pyが見つからない場合は、以下のようなエラーメッセージ(No such file or directory)が表示されます。

```{index} Error message
```

(exec-fizzbuzz-error)=

```{code-block} text
:caption: "fizzbuzz.pyの実行"

$ python fizzbuzz.py
can't open file 'fizzbuzz.py': [Errno 2] No such file or directory
```

```{index} for
```

### for文

「1から100までのFizzBuzzを表示する」ために `fizzbuzz()` 関数に1から100までの数値を順に与えます。

`for` 文を使って繰り返し処理を実装しましょう（{numref}`for`）。

(for)=

```{code-block} python
:caption: "for文と関数の実行"
:emphasize-lines: 4-5

def fizzbuzz(num):
    return num

for num in range(1, 101):
    print(fizzbuzz(num))
```

(fizzbuzz-2)=

```{code-block} bash
:caption: "fizzbuzz.pyの実行(2)"

$ python fizzbuzz.py
1
2
3
.
.
100
```

{numref}`fizzbuzz-2` のように、実行すると1から100までの数字が表示されます。

```{index} range()
```

数字を順番に使って処理したい場合、組み込み関数 range() が便利です。

range(1, 101)のように記述すると、1から100までの数字を順番に得ることができ、

結果として `fizzbuzz()` 関数には1 から100までの数字が順に与えられています。

現時点の `fizzbuzz()` 関数は与えられた引数をそのまま返す実装なので、これで問題ありません。

```{hint}
[for文の動作を確認(Python Tutor)](https://pythontutor.com/render.html#code=def%20fizzbuzz%28num%29%3A%0A%20%20%20%20return%20num%0A%0Afor%20num%20in%20range%281,%20101%29%3A%0A%20%20%20%20print%28fizzbuzz%28num%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false)

<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=def%20fizzbuzz%28num%29%3A%0A%20%20%20%20return%20num%0A%0Afor%20num%20in%20range%281,%20101%29%3A%0A%20%20%20%20print%28fizzbuzz%28num%29%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>
```

for文は次のように書きます。

```none
for ＜変数名＞ in ＜シーケンス＞:
```

`＜変数名＞` にはループ内で繰り返される変数名、 `＜シーケンス＞` には繰り返しのための変数（繰り返し可能な型(シーケンス)のオブジェクト）を書きます。

{numref}`for` では、繰り返される変数 `num` が `fizzbuzz()` 関数に渡されています。

繰り返しのための変数は `range(1, 101)` の実行結果（1から100までのイテレータ）です。

関数の結果として数値が順番に返され、ひとつひとつの数字が繰り返し用の変数（`num`）に渡され、 `for` のブロックが実行されます

```{index} if
```

### if文

FizzBuzzの処理を作るには、引数の数字（`num`）に応じて処理を分岐する必要があります。

処理の流れとしては次のようになります。

1. 引数 `num` を受け取る
2. `num` と3の剰余が0（3で割り切れる）、かつ `num` と5の剰余が0である（5で割り切れる）場合に、 `'FizzBuzz'` を返す
3. `num` と3の剰余が0の場合に、 `'Fizz'` を返す
4. `num` と5の剰余が0の場合に、 `'Buzz'` を返す
5. 2〜4のどれでもない場合、引数 `num` を文字列にして返す

Pythonで条件による処理の分岐を扱うにはif文を使います。

`fizzbuzz()` 関数は、 {numref}`if` のようになります。

(if)=

```{code-block} python
:caption: "fizzbuzz関数を完成させる"
:emphasize-lines: 2-9

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return str(num)

for num in range(1, 101):
    print(fizzbuzz(num))
```

紹介していない要素がいくつか登場しています。

```{index} pair: if; elif pair: if; else
```

#### `if` 文

`if` 文は、条件に与えられた式が真と評価できる場合に、 `if` ブロックの処理を実行します。

`elif` 文は、 `if` 文の条件が偽の場合に、追加の条件を与えます。追加の条件が真の場合に、 `elif` ブロックの処理を実行します。

`else` ブロックは、どの条件にも当てはまらない場合に実行されます。

```{index} ==
```

```{index} and
```

```{index} str()
```

#### 演算子

`==` は比較演算子の1つで、左辺と右辺の値が同じ場合に真（`True`） を返します。それ以外の場合には偽（`False`）を返します。

`and` はブール演算子の1つで、左右の条件が `True` の場合に `True` を返します（より正確には、左の条件が真と評価できる場合に右を評価して結果を返します）。

#### `str()` 関数

引数を文字列に変換して返します。

```{hint}
[if文の動作を確認(Python Tutor)](https://pythontutor.com/render.html#code=def%20fizzbuzz%28num%29%3A%0A%20%20%20%20if%20num%20%25%203%20%3D%3D%200%20and%20num%20%25%205%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20return%20'FizzBuzz'%0A%20%20%20%20elif%20num%20%25%203%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20return%20'Fizz'%0A%20%20%20%20elif%20num%20%25%205%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20return%20'Buzz'%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%20str%28num%29%0A%0Afor%20num%20in%20range%281,%20101%29%3A%0A%20%20%20%20print%28fizzbuzz%28num%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false)

<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=def%20fizzbuzz%28num%29%3A%0A%20%20%20%20if%20num%20%25%203%20%3D%3D%200%20and%20num%20%25%205%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20return%20'FizzBuzz'%0A%20%20%20%20elif%20num%20%25%203%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20return%20'Fizz'%0A%20%20%20%20elif%20num%20%25%205%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20return%20'Buzz'%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%20str%28num%29%0A%0Afor%20num%20in%20range%281,%20101%29%3A%0A%20%20%20%20print%28fizzbuzz%28num%29%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>
```

### FizzBuzz処理の実装の完了

これで `fizzbuzz()` 関数の実装が完了しました。

`fizzbuzz.py` を実行しましょう。 {numref}`fizzbuzz-out` のような結果になります。

(fizzbuzz-out)=

```{code-block} bash
:caption: "完成したfizzbuzz.pyの実行"

$ python fizzbuzz.py
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
.
.
Buzz
```

おめでとうございます！ これがPythonの第一歩です。

FizzBuzz はいろいろな方法で実装できます。もっと短く、わかりやすく書くにはどうすればよいか、チャレンジしてみてください。

:::{admonition} コラム: 値には型がある
Pythonでは整数や文字列、リストなど多種多様な値を使うことができますが、これらを区別して扱うための仕組みがあります。この仕組みのことを `型` といいます。

型ごとにできることとできないことが定義されていて、それぞれの値は型のインスタンスになります。
数値の `100` は整数型（int）の値で、他の数値と演算ができます。

また、ある値の型は他の抽象度が高い型のものとみなすことができるものもあります。
たとえば文字列やリストの型は、それぞれ文字列型（str）のとリスト型（list）ですが、ほかに繰り返し可能な型（シーケンス）ともいえます。

型は組み込み関数の `type()` 関数や `isinstance()` 関数を使って調べることができます。

```{code-block} python
:caption: "文字列とリストとそれらの型"

>>> n1 = 100
>>> s1 = "hello"
>>> l1 = [1, 2, 3]
>>> type(n1)
<class 'int'>
>>> type(s1)
<class 'str'>
>>> type(l1)
<class 'list'>
>>> isinstance(n1, int)
True
>>> isinstance(s1, str)
True
>>> isinstance(l1, list)
True
>>> import collections.abc
>>> isinstance(s1, collections.abc.Sequence)
True
>>> isinstance(l1, collections.abc.Sequence)
True
```
:::

## まとめ

本節では、FizzBuzzを通じたPythonの特徴、基本を紹介しました。

次節では、Pythonの基本のデータ型について説明します。
