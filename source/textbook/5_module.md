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

### 作業用フォルダの作成と現在のフォルダの移動

作業前に、ファイル操作で利用するフォルダ「pycamp」を作成します。

```{code-block} bash
:caption: "作業用フォルダの作成(macOS、Linuxの場合)"

$ cd ~/
$ mkdir pycamp
$ cd pycamp
```

```{code-block} doscon
:caption: "作業用フォルダの作成(Windowsの場合)"

cd ~
mkdir pycamp
cd pycamp
```

### ファイルのオープン(書き込みモード)

まずはPythonでファイルに書き込んでみます。

Pythonでファイルを書き込むために、ファイルを開く必要があります。
Pythonでファイルを開くには `open()` 関数を使います。
書き込み用にファイルを開く場合には、以下のように引数を指定してファイルを **書き込みモード** で開きます。

|引数|内容|
|---|---|
|第1引数| ファイルのパス|
|第2引数|ファイルのモード(この場合は `w` で書き込みモード)|
|encoding引数|ファイルの文字コード(この場合は `utf-8`)|

以下のように指定して `pycamp.txt` というファイルを書き込みモードで開きます( {numref}`file-open` )。

(file-open)=

```{code-block} pycon
:caption: "ファイルを開く"

>>> f = open('pycamp.txt', 'w', encoding='utf-8')
>>> f
<_io.TextIOWrapper name='pycamp.txt' mode='w' encoding='utf-8'>
```

`open()` 関数は、ファイルオブジェクトを返します（{numref}`file-open` の場合は `f` へ代入しています）。
ファイルオブジェクトを通じて、開いたファイルに対する書き込みや読み込みの操作を行います。

```{tip}
ファイルが存在しない状態で書き込みモードでファイルを開くと、ファイルが新規に作成されます。

ファイルが存在する場合は、もとの中身が削除されます。大事なファイルの中身を書き込みモードで消さないように注意してください。
```

```{index} write() single: Files; write()
```

### ファイルへの書き込み

ファイルへ書き込みを行うには、ファイルオブジェクトの `.write()` メソッドを使用します。
引数に書き込む文字列を指定します（{numref}`write-string`）。
`.write()` メソッドを実行すると、書き込んだ文字数が返されます。

(write-string)=

```{code-block} pycon
:caption: "ファイルへ書き込み"

>>> f.write('Hello')
5
>>> f.write(' Python\n')  # 改行を書き込むには \n を指定する
8
>>> f.write('こんにちはPython\n')  # 日本語も書き込み可能
12
```

```{index} close() single: File; close()
```

### ファイルのクローズ

ファイルを開いた後は閉じる必要があります。ファイルを閉じることにより、ファイルを開くために使われていたシステム資源を解放します。

ファイルを閉じるには、ファイルオブジェクトの `.close()` メソッドを呼び出します。

(file-close)=

```{code-block} pycon
:caption: "ファイルを閉じる"

>>> f.close()
```

{numref}`file-open`、{numref}`write-string`、{numref}`file-close` の結果、実行環境直下に `pycamp.txt` というファイルが次のような内容で作成されます。

```{code-block} none
:caption: "新規作成されたpycamp.txtの内容"

Hello Python
こんにちはPython
```


```{index} read() single: File; read()
```

### ファイルの読み込み

ファイルの中身を読み込むには、ファイルを読み込みモード(`r`)で開きます。
その後ファイルオブジェクトの `.read()` メソッドでファイルの中身を読み込みます（{numref}`read-file`）。

(read-file)=

```{code-block} pycon
:caption: "ファイル内容の読み込み"

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
:caption: "第2引数を省略してファイルを開く"

>>> f = open('pycamp.txt', encoding='utf-8')
>>> f
<_io.TextIOWrapper name='pycamp.txt' mode='r' encoding='utf-8'>
```

:::{note}
with文でのファイルオープン

ファイルを扱う際には、 [with文](https://docs.python.org/ja/3/reference/compound_stmts.html#with) を使うと便利です。
`with` 文を使うことで、ファイルのクローズを自動で行えます。処理中に例外が発生しても必ずファイルを閉じることができます。

`with` 文を使うと、ファイルのオープン、書き込み、読み込み、クローズの処理は、{numref}`with-statement` のように書き換えられます。

(with-statement)=

```{code-block} pycon
:caption: "ファイルオープンとwith文"

>>> # 書き込み
>>> with open('pycamp.txt', 'w', encoding='utf-8') as f:
...     f.write('Hello')
...     f.write(' Python\n')
...     f.write('こんにちはPython\n')
...
5
8
12
>>> # 読み込み
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
:caption: "追記モードでファイルを開く"

>>> f = open('pycamp.txt', 'a', encoding='utf-8')
>>> f.write('こんにちは世界\n')
8
>>> f.close()
```

{numref}`append-mode` の結果、追記後の `pycamp.txt` の内容は次のようになります

```{code-block} none
:caption: "追記されたpycamp.txtの内容"

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
:caption: "add()、sub()関数の定義（calc.py）"

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
:caption: "calcのインポート"

>>> import calc
```

`calc` というモジュールがインポートされました。

Pythonファイルをインポートすることでモジュール（module）として再利用できます。

`calc` モジュールから `add()` 関数を使うには、 `calc.add()` と呼び出します（{numref}`call-calc-add`）。

(call-calc-add)=

```{code-block} pycon
:caption: "別モジュールの関数を利用"

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
:caption: "関数のインポート"

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
:caption: "インポート対象に別名をつける"

>>> import calc as c
>>> c.add(1, 2)
3
```

### 複数の対象をインポート

`calc` モジュールから `add()` 、 `sub()` 関数を一度にインポートするには、
`import` 文でインポート対象をカンマ区切りで指定します({numref}`import-functions`)。

(import-functions)=

```{code-block} pycon
:caption: "複数の対象をインポート"

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
:caption: "括弧を使った複数のインポート"

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
:caption: "datetime.date()コンストラクタ"

>>> import datetime
>>> d = datetime.date(2016, 12, 23)
>>> print(d.year, d.month, d.day)
2016 12 23
```

また、 `datetime.date.today()` メソッドを使うと今日の日付を取得することができます。

```{code-block} pycon
:caption: "datetime.date.today()メソッド"

>>> today = datetime.date.today()
>>> print(today)  # 実行する日によって結果が異なる
2018-02-17
```

ここで、自分が生まれてから今日までに何日経過したのかを計算してみましょう。
自分で実装しようとすると、月ごとに日数が違う、うるう年の計算など面倒な計算が必要となりますが、
`datetime.date` を使うと面倒な部分をモジュールが肩代わりしてくれます。

```{code-block} pycon
:caption: "datetime.date.today()メソッド"

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
:caption: "reモジュールの利用"

>>> import re
>>> m = re.search('(P(yth|l)|Z)o[pn]e?', 'Python')
>>> m
<re.Match object; span=(0, 6), match='Python'>
```

正規表現にマッチした場合、 `re.search()` は結果を表すマッチオブジェクトを返します。
マッチオブジェクトから値を取り出すには、 `.group()` メソッドを呼び出します（{numref}`match-object`）。

(match-object)=

```{code-block} pycon
:caption: "正規表現にマッチした文字列の取得"

>>> m.group()
'Python'
```

正規表現がグループを含む場合、グループの番号を引数に渡して取り出せます。
引数を指定しないか、0を指定すると、正規表現全体のマッチが返されます（{numref}`match-group`）。

(match-group)=

```{code-block} pycon
:caption: "グループを指定して文字列の取得"

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
:caption: "正規表現にマッチしない場合"

>>> re.search('py', 'ruby')
>>>
```

```{admonition} コラム: 正規表現の文字列
正規表現の文字列にはPythonのraw文字列を使うのが一般的です。

`r` プレフィックスをつけてraw文字列を定義します。
raw文字列ではバックスラッシュを特別扱いしないので、
正規表現中にバックスラッシュを使う際に `'\\'` と書く必要がなくなります。
```

`re` モジュールには、ここで説明していない有効な使い方があります。
Pythonの公式ドキュメントの「 [reモジュール](https://docs.python.org/ja/3/library/re.html) 」を参考にしてください。

また、他のPython標準ライブラリについては、「 [Python標準ライブラリ](https://docs.python.org/ja/3/library/index.html) 」を参考にしてください。

## まとめ

本節では、Pythonでファイルを読み書きする方法、Pythonファイルを分割して再利用する方法を解説しました。
また、標準ライブラリである `datetime` モジュールや `re` モジュールの紹介をしました。
