# ファイル操作とモジュール

本節では、Pythonでファイルを読み書きする方法と、
Pythonファイルの分割と再利用のためモジュールについて説明します。
また、Pythonが用意するモジュールである標準ライブラリも紹介します。

```{index} Files
```

(guide-files)=

## ファイル操作

プログラムには何らかの入出力が不可欠です。ここでは入力元、出力先としてファイルを操作する方法を説明します。

```{index} open() single: Files; open()
```

### ファイルのオープン(書き込みモード)

まずはPythonでファイルに書き込んでみます。

Pythonでファイルを書き込むために、ファイルを開く必要があります。
Pythonでファイルを開くには `open()` 関数を使います。
書き込み用にファイルを開く場合には、以下のように引数を指定してファイルを **書き込みモード** で開きます。

```{eval-rst}

:第1引数: ファイルのパス
:第2引数: ファイルのモード(この場合は ``w`` で書き込みモード)
:encoding引数: ファイルの文字コード(この場合は ``utf-8``)
```

以下のように指定して `pycamp.txt` というファイルを書き込みモードで開きます( {numref}`file-open` )。

(file-open)=

```{code-block} pycon
:caption: "\u30D5\u30A1\u30A4\u30EB\u3092\u958B\u304F"

>>> f = open('pycamp.txt', 'w', encoding='utf-8')
>>> f
<_io.TextIOWrapper name='pycamp.txt' mode='w' encoding='utf-8'>
```

`open()` 関数は、ファイルオブジェクトを返します（{numref}`file-open` の場合は `f` へ代入しています）。
ファイルオブジェクトを通じて、開いたファイルに対する書き込みや読み込みの操作を行います。

:::{tip}
ファイルが存在しない状態で書き込みモードでファイルを開くと、ファイルが新規に作成されます。

ファイルが存在する場合は、もとの中身が削除されます。大事なファイルの中身を書き込みモードで消さないように注意してください。
:::

```{index} write() single: Files; write()
```

### ファイルへの書き込み

ファイルへ書き込みを行うには、ファイルオブジェクトの `.write()` メソッドを使用します。
引数に書き込む文字列を指定します（{numref}`write-string`）。
`.write()` メソッドを実行すると、書き込んだ文字数が返されます。

(write-string)=

```{code-block} pycon
:caption: "\u30D5\u30A1\u30A4\u30EB\u3078\u66F8\u304D\u8FBC\u307F"

>>> f.write('Hello')
5
>>> f.write(' Python\n')  # 改行を書き込むには \n を指定する
8
>>> f.write('こんにちはPython\n')  # 日本語も書き込み可能
12
```

{numref}`file-open`、{numref}`write-string` の結果、実行環境直下に `pycamp.txt` というファイルが次のような内容で作成されます。

```{code-block} none
:caption: "\u65B0\u898F\u4F5C\u6210\u3055\u308C\u305Fpycamp.txt\u306E\u5185\u5BB9"

Hello Python
こんにちはPython
```

```{index} close() single: File; close()
```

### ファイルのクローズ

ファイルを開いた後は閉じる必要があります。ファイルを閉じることにより、ファイルを開くために使われていたシステム資源を解放します。

ファイルを閉じるには、ファイルオブジェクトの `.close()` メソッドを呼び出します。

```{code-block} pycon
:caption: "\u30D5\u30A1\u30A4\u30EB\u3092\u9589\u3058\u308B"

>>> f.close()
```

```{index} read() single: File; read()
```

### ファイルの読み込み

ファイルの中身を読み込むには、ファイルを読み込みモード(`r`)で開きます。
その後ファイルオブジェクトの `.read()` メソッドでファイルの中身を読み込みます（{numref}`read-file`）。

(read-file)=

```{code-block} pycon
:caption: "\u30D5\u30A1\u30A4\u30EB\u5185\u5BB9\u306E\u8AAD\u307F\u8FBC\u307F"

>>> f = open('pycamp.txt', 'r', encoding='utf-8')
>>> f
<_io.TextIOWrapper name='pycamp.txt' mode='r' encoding='utf-8'>
>>> txt = f.read()
>>> print(txt)
Hello Python
こんにちはPython
>>> f.close()
```

`.read()` メソッドは、ファイルの内容の文字列（`str`）を返します。

なお、第2引数のデフォルトは読み込みモードなので、 `r` の指定は省略できます({numref}`read-file2`)。

(read-file2)=

```{code-block} pycon
:caption: "\u7B2C2\u5F15\u6570\u3092\u7701\u7565\u3057\u3066\u30D5\u30A1\u30A4\u30EB\
:  \u3092\u958B\u304F"

>>> f = open('pycamp.txt', encoding='utf-8')
>>> f
<_io.TextIOWrapper name='pycamp.txt' mode='r' encoding='utf-8'>
```

:::{note}
with文でのファイルオープン

ファイルを扱う際には、 [with文](https://docs.python.org/ja/3/reference/compound_stmts.html#with) を使うと便利です。
`with` 文を使うことで、ファイルのクローズを自動で行えます。処理中に例外が発生しても必ずファイルを閉じることができます。

`with` 文を使うと、ファイルのオープン、読み込み、クローズの処理は、{numref}`with-statement` のように書き換えられます。

(with-statement)=

```{code-block} pycon
:caption: "\u30D5\u30A1\u30A4\u30EB\u30AA\u30FC\u30D7\u30F3\u3068with\u6587"

>>> with open('pycamp.txt', encoding='utf-8') as f:
...     txt = f.read()
...
>>> print(txt)
Hello Python
こんにちはPython
```
:::

```{index} append mode single: File; append mode
```

### 追記モードでの書き込み

書き込みモード(`'w'`)でファイルを開くと、ファイルの内容は常に新しく上書きされます。

{numref}`write-string` の書き込みをもう一度行っても、ファイルの内容は `'Hello Python\nこんにちはPython\n'` となります。

すでに存在するファイルを対象に、末尾に追記するには、ファイルを追記モードで開きます。
追記モードでファイルを開くには、 `open()` 関数の第2引数に `'a'` を指定します（{numref}`append-mode`）。

(append-mode)=

```{code-block} pycon
:caption: "\u8FFD\u8A18\u30E2\u30FC\u30C9\u3067\u30D5\u30A1\u30A4\u30EB\u3092\u958B\
:  \u304F"

>>> f = open('pycamp.txt', 'a', encoding='utf-8')
>>> f.write('こんにちは世界\n')
8
```

{numref}`append-mode` の結果、追記後の `pycamp.txt` の内容は次のようになります

```{code-block} none
:caption: "\u8FFD\u8A18\u3055\u308C\u305Fpycamp.txt\u306E\u5185\u5BB9"

Hello Python
こんにちはPython
こんにちは世界
```

```{index} Module
```

(guide-module)=

## モジュール

ここまでの処理はPythonインタープリタの対話モード上か、1つのPythonファイルに記述して実行してきました。

しかし、対話モード上では処理を残すことができませんし、1つのファイルに記述していると、プログラムが長くなるとどこに何を書いているのかがわからなくなってきます。

処理が長く、複雑になると、複数のファイルに処理を分割する必要があります。役割ごとにファイルを分割することで、それぞれどういった処理をするものかを明確にできます。

Pythonでは他のPythonファイルや関数をインポート（import）して再利用できます。処理を複数のファイルに分割し、必要な処理をインポートして使います。

実行環境直下に `calc.py` というファイルを作成して、 `add()` 、 `sub()` 関数を定義しましょう（{numref}`calc-py`）。

(calc-py)=

```{code-block} python
:caption: "add()\u3001sub()\u95A2\u6570\u306E\u5B9A\u7FA9\uFF08calc.py\uFF09"

def add(a, b):
    return a + b


def sub(a, b):
    return a - b
```

```{index} import single: Module; import
```

別のファイルをインポートするには `import` 文を使います。

Pythonインタープリタを起動して、 `calc.py` をインポートしましょう（{numref}`import-calc`）。

(import-calc)=

```{code-block} pycon
:caption: "calc\u306E\u30A4\u30F3\u30DD\u30FC\u30C8"

>>> import calc
```

`calc` というモジュールがインポートされました。

Pythonファイルをインポートすることでモジュール（module）として再利用できます。

`calc` モジュールから `add()` 関数を使うには、 `calc.add()` と呼び出します（{numref}`call-calc-add`）。

(call-calc-add)=

```{code-block} pycon
:caption: "\u5225\u30E2\u30B8\u30E5\u30FC\u30EB\u306E\u95A2\u6570\u3092\u5229\u7528"

>>> calc.add(1, 2)
3
```

```{index} from single: Module; from
```

### 関数のインポート

`add()` 関数を直接インポートするには、 `from ＜モジュール＞ import ＜インポート対象＞` 文を使います。

`from ＜モジュール＞` の部分にモジュール、 `import ＜インポート対象＞` の部分にインポートの対象を書きます（{numref}`import-function`）。

(import-function)=

```{code-block} pycon
:caption: "\u95A2\u6570\u306E\u30A4\u30F3\u30DD\u30FC\u30C8"

>>> from calc import add
>>> add(1, 2)
3
```

```{index} as single: Module; as
```

### 別名をつける

インポートした関数やモジュールに別名をつけるには `as` を使います。
関数やモジュールが頻繁に使われるのに名前が長い場合に使われます。

`import <インポート対象> as <別名>` のように別名を指定します。
`calc` モジュールに別名 `c` をつけてインポートするには {numref}`import-as` のようにします。

(import-as)=

```{code-block} pycon
:caption: "\u30A4\u30F3\u30DD\u30FC\u30C8\u5BFE\u8C61\u306B\u5225\u540D\u3092\u3064\
:  \u3051\u308B"

>>> import calc as c
>>> c.add(1, 2)
3
```

### 複数の対象をインポート

`calc` モジュールから `add()` 、 `sub()` 関数を一度にインポートするには、
`import` 文でカンマ区切りでインポート対象を指定します({numref}`import-functions`)。

(import-functions)=

```{code-block} pycon
:caption: "\u8907\u6570\u306E\u5BFE\u8C61\u3092\u30A4\u30F3\u30DD\u30FC\u30C8"

>>> from calc import add, sub
>>> add(1, 2)
3
>>> sub(2, 1)
1
```

また、 {numref}`import-functions2` のように括弧を使っても指定できます。
インポート対象が多い場合は括弧を使った書き方のほうが可読性が高いので、こちらを使います。

(import-functions2)=

```{code-block} pycon
:caption: "\u62EC\u5F27\u3092\u4F7F\u3063\u305F\u8907\u6570\u306E\u30A4\u30F3\u30DD\
:  \u30FC\u30C8"

>>> from calc import (
...     add,
...     sub,
... )
```

```{index} Standard library
```

## 標準ライブラリの利用

Python自体も標準でモジュールを提供しています。これら標準で提供されているモジュールをまとめて標準ライブラリと呼びます。

必要な処理をすべて自分で実装するのでなく、積極的に標準ライブラリを利用しましょう。

標準ライブラリを利用すると重複する実装が減り、コードの記述量を大幅に削減できます。

```{index} datetime single: Standard library; datetime
```

### 日付を扱うモジュール

標準ライブラリの1つ `datetime` モジュールを取り上げます。
`datetime` は日付や時刻を簡単に扱うことができるモジュールです。
ここでは例として日付の計算をします。

`datetime.date()` コンストラクタを使って日付を意味するオブジェクトを生成できます。
引数として年、月、日を指定します。

```{code-block} pycon
:caption: "datetime.date()\u30B3\u30F3\u30B9\u30C8\u30E9\u30AF\u30BF"

>>> import datetime
>>> d = datetime.date(2016, 12, 23)
>>> print(d.year, d.month, d.day)
2016 12 23
```

また、 `datetime.date.today()` メソッドを使うと今日の日付を取得することができます。

```{code-block} pycon
:caption: "datetime.date.today()\u30E1\u30BD\u30C3\u30C9"

>>> today = datetime.date.today()
>>> print(today)  # 実行する日によって結果が異なる
2018-02-17
```

ここで、自分が生まれてから今日までに何日経過したのかを計算してみましょう。
自分で実装しようとすると、月ごとに日数が違う、うるう年の計算など面倒な計算が必要となりますが、
`datetime.date` を使うと面倒な部分をモジュールが肩代わりしてくれます。

```{code-block} pycon
:caption: "datetime.date.today()\u30E1\u30BD\u30C3\u30C9"

>>> birthday = datetime.date(2008, 12, 3)  # Python 3.0のリリース日
>>> today = datetime.date.today()
>>> delta = today - birthday  # 日付や時刻の差を表すdatetime.timedeltaオブジェクト
>>> print(delta.days)  # 実行する日によって結果が異なる
3363
```

`datetime` モジュールは他にも時刻を扱う `datetime.time`, 日付と時刻両方を扱う `datetime.datetime` など日付や時刻の計算に便利な関数がたくさんあります。
詳しくはPythonの公式ドキュメントの「 [datetimeモジュール](https://docs.python.org/ja/3/library/datetime.html) 」を参考にしてください。

```{index} re single: Standard library; re
```

### 正規表現モジュール

次に標準ライブラリの1つ `re` モジュールを扱います。
`re` モジュールはPythonで正規表現を扱うためのモジュールです。

`re.search()` 関数を使って、文字列が正規表現にマッチするか調べられます。第1引数に正規表現、第2引数に対象の文字列を渡します（{numref}`re-module`）。

(re-module)=

```{code-block} pycon
:caption: "re\u30E2\u30B8\u30E5\u30FC\u30EB\u306E\u5229\u7528"

>>> import re
>>> m = re.search('(P(yth|l)|Z)o[pn]e?', 'Python')
>>> m
<_sre.SRE_Match object; span=(0, 6), match='Python'>
```

正規表現にマッチした場合、 `re.search()` は結果を表すマッチオブジェクトを返します。
マッチオブジェクトから値を取り出すには、 `.group()` メソッドを呼び出します（{numref}`match-object`）。

(match-object)=

```{code-block} pycon
:caption: "\u6B63\u898F\u8868\u73FE\u306B\u30DE\u30C3\u30C1\u3057\u305F\u6587\u5B57\
:  \u5217\u306E\u53D6\u5F97"

>>> m.group()
'Python'
```

正規表現がグループを含む場合、グループの番号を引数に渡して取り出せます。
引数を指定しないか、0を指定すると、正規表現全体のマッチが返されます（{numref}`match-group`）。

(match-group)=

```{code-block} pycon
:caption: "\u30B0\u30EB\u30FC\u30D7\u3092\u6307\u5B9A\u3057\u3066\u6587\u5B57\u5217\
:  \u306E\u53D6\u5F97"

>>> m = re.search('py(thon)', 'python')
>>> m.group()
'python'
>>> m.group(0)
'python'
>>> m.group(1)
'thon'
```

正規表現にマッチしない場合は、{numref}`not-match` に示すように何も返しません（`None` を返します）。

(not-match)=

```{code-block} pycon
:caption: "\u6B63\u898F\u8868\u73FE\u306B\u30DE\u30C3\u30C1\u3057\u306A\u3044\u5834\
:  \u5408"

>>> re.search('py', 'ruby')
>>>
```

:::{admonition} コラム: 正規表現の文字列
正規表現の文字列にはPythonのraw文字列を使うのが一般的です。

`r` プレフィックスをつけてraw文字列を定義します。
raw文字列ではバックスラッシュを特別扱いしないので、
正規表現中にバックスラッシュを使う際に `'\\'` と書く必要がなくなります。
:::

`re` モジュールには、ここで説明していない有効な使い方があります。
Pythonの公式ドキュメントの「 [reモジュール](https://docs.python.org/ja/3/library/re.html) 」を参考にしてください。

また、他のPython標準ライブラリについては、「 [Python標準ライブラリ](https://docs.python.org/ja/3/library/index.html) 」を参考にしてください。

## まとめ

本節では、Pythonでファイルを読み書きする方法、Pythonファイルを分割して再利用する方法を解説しました。
また、標準ライブラリである `datetime` モジュールや `re` モジュールの紹介をしました。
