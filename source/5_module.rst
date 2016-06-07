==================================
ファイル操作とモジュール
==================================

本節では、Pythonでファイルを読み書きする方法と、
Pythonファイルの分割と再利用のためモジュールについて説明します。

.. _guide-files:

ファイル操作
===============

プログラムには何らかの入出力が不可欠です。ここでは入力元、出力先としてファイルを操作する方法を説明します。

ファイルのオープン
------------------------

Pythonからファイルを読み込む前に、現在のディレクトリ直下に ``todo.txt`` というファイルを作成しましょう。

内容は、:numref:`todo-txt` のようにします。

.. _todo-txt:

.. code-block:: none
   :caption: todo.txt

   Write the book
   Try new python libraries

Pythonでファイルを開くには ``open()`` 関数を使います。
第1引数にファイルのパスを指定します。

:numref:`todo-txt` のtodo.txtを開くには、:numref:`file-open` のように指定します

.. _file-open:

.. code-block:: python
    :caption: ファイルを開く

    >>> f = open('todo.txt')
    >>> f
    <_io.TextIOWrapper name='todo.txt' mode='r' encoding='UTF-8'>

``open()`` 関数は、ファイルオブジェクト（:numref:`file-open` の場合はf）を返します。
ファイルオブジェクトは実際のファイルに対応するオブジェクトです。

ファイルの読み込み
----------------------

ファイルの内容を読み込むには、ファイルオブジェクトの ``.read()`` メソッドを呼び出します（:numref:`read-file`）。

.. _read-file:

.. code-block:: python
    :caption: ファイル内容の読み込み

    >>> todo_str = f.read()
    >>> print(todo_str)
    Write the book
    Try new python libraries

``.read()`` メソッドは、ファイルの内容の文字列（``str``）を返します。

ファイルのクローズ
------------------
ファイルを使った後は閉じる必要があります。クローズにより、ファイルを開くために使われていたシステム資源を解放します。

ファイルを閉じるには、ファイルオブジェクトの ``.close()`` メソッドを呼び出します。

.. code-block:: python
    :caption: ファイルを閉じる

    >>> f.close()

ファイルを扱う際には、 `with文 <http://docs.python.jp/2.7/reference/compound_stmts.html#with>`_ を使うと便利です。
``with`` 文を使うことで、ファイルのクローズを自動で行えます。処理中に例外が発生しても必ずファイルを閉じることができます。

``with`` 文を使うと、ファイルのオープン、読み込み、クローズの処理は、:numref:`with-statement` のように書き換えられます。

.. _with-statement:

.. code-block:: python
    :caption: ファイルオープンとwith文

    >>> with open('todo.txt') as f:
    ...     todo_str = f.read()
    ...
    >>> print(todo_str)

ファイルへの書き込み
----------------------------
ファイルへ書き込む場合にも、最初に ``open()`` 関数を使ってファイルを開きます。
その際、第2引数に ``'w'`` を渡します。これでファイルを「書き込みモード」で開けます
（第2引数を渡さない場合は、読み込みモード（``'r'``）で開かれます）。

``memo.txt`` というファイルを実行環境直下に作る例を :numref:`write-mode` に示します。

.. _write-mode:

.. code-block:: python
    :caption: 書き込みモードでファイルを開く

    >>> f = open('memo.txt', 'w')
    >>> f
    <_io.TextIOWrapper name='memo.txt' mode='w' encoding='UTF-8'>

書き込みを行うには ``.write()`` メソッドを使います。
引数に文字列を渡して書き込みます（:numref:`write-string`）。

.. _write-string:

.. code-block:: python
    :caption: ファイル内容の書き込み

    >>> f.write('Hello')
    5
    >>> f.write(' world\n')
    7

:numref:`write-mode`、:numref:`write-string` の結果、実行環境直下に ``memo.txt`` というファイルが次のような内容で作成されます。

.. code-block:: none
    :caption: 新規作成されたmemo.txtの内容

    Hello world

追記モードでの書き込み
-------------------------------

書き込みモードでファイルを開くと、ファイルの内容は常に新しく上書きされます。

:numref:`write-string` の書き込みをもう一度行っても、ファイルの内容は ``'Hello world'`` になります。

すでに存在するファイルを対象に、末尾に追記するには、ファイルを追記モードで開きます。
追記モードでファイルを開くには、 ``open()`` 関数の第2引数に ``'a'`` を指定します（:numref:`append-mode`）。

.. _append-mode:

.. code-block:: python
    :caption: 追記モードでファイルを開く

    >>> f = open('memo.txt', 'a')
    >>> f.write('こんにちは世界\n')
    8

:numref:`append-mode` の結果、追記後の ``memo.txt`` の内容は次のようになります

.. code-block:: none
    :caption: 追記されたmemo.txtの内容

    Hello world
    こんにちは世界

.. _guide-module:

モジュール
=====================

ここまでの処理はPythonインタープリタ上か、1つのファイルに記述してきました。

しかし、インタープリタ上では処理を残すことができませんし、1つのファイルに記述しているとどこに何を書いているのかがわからなくなってきます。

処理が長く、複雑になると、複数のファイルに処理を分割する必要があります。役割ごとにファイルを分割することで、それぞれどういった処理をするものかを明確にできます。

Pythonでは他のPythonファイルや関数をインポート（import）して再利用できます。処理を複数のファイルに分割し、必要な処理をインポートして使います。

実行環境直下に ``calc.py`` というファイルを作成して、 ``add()`` 、 ``sub()`` 関数を定義しましょう（:numref:`calc-py`）。

.. _calc-py:

.. code-block:: python
    :caption: add()、sub()関数の定義（calc.py）

    def add(a, b):
        return a + b


    def sub(a, b):
        return a - b

別のファイルをインポートするには ``import`` 文を使います。

Pythonインタープリタを起動して、 ``calc.py`` をインポートしましょう（:numref:`import-calc`）。

.. _import-calc:

.. code-block:: python
    :caption: calcのインポート

    >>> import calc

``calc`` というモジュールがインポートされました。

Pythonファイルをインポートすることでモジュール（module）として再利用できます。

``calc`` モジュールから ``add()`` 関数を使うには、 ``calc.add()`` と呼び出します（:numref:`call-calc-add`）。

.. _call-calc-add:

.. code-block:: python
    :caption: 別モジュールの関数を利用

    >>> calc.add(1, 2)
    3

関数のインポート
-------------------------

``add()`` 関数を直接インポートするには、 ``from ＜モジュール＞ import ＜インポート対象＞`` 文を使います。

``from ＜モジュール＞`` の部分にモジュール、 ``import ＜インポート対象＞`` の部分にインポートの対象を書きます（:numref:`import-function`）。

.. _import-function:

.. code-block:: python
    :caption: 関数のインポート

    >>> from calc import add
    >>> add(1, 2)
    3

別名をつける
----------------

インポートした関数やモジュールに別名をつけるには ``as`` を使います。
関数やモジュールが頻繁に使われるのに名前が長い場合に使われます。

``import <インポート対象> as <別名>`` のように別名を指定します。
``calc`` モジュールに別名 ``c`` をつけてインポートするには :numref:`import-as` のようにします。

.. _import-as:

.. code-block:: python
    :caption: インポート対象に別名をつける

    >>> import calc as c
    >>> c.add(1, 2)
    3

複数の対象をインポート
-----------------------------------

``calc`` モジュールから ``add()`` 、 ``sub()`` 関数を一度にインポートするには、
``import`` 文でカンマ区切りでインポート対象を指定します(:numref:`import-functions`)。

.. _import-functions:

.. code-block:: python
    :caption: 複数の対象をインポート

    >>> from calc import add, sub
    >>> add(1, 2)
    3
    >>> sub(2, 1)
    1

また、 :numref:`import-functions2` のように括弧を使っても指定できます。
インポート対象が多い場合は括弧を使った書き方のほうが可読性が高いので、こちらを使います。

.. _import-functions2:

.. code-block:: python
    :caption: 括弧を使った複数のインポート

    >>> from calc import (
    ...     add,
    ...     sub,
    ... )

標準ライブラリの利用
=====================================

Python自体も標準でモジュールを提供しています。これら標準で提供されているモジュールをまとめて標準ライブラリと呼びます。

必要な処理をすべて自分で実装するのでなく、積極的に標準ライブラリを利用しましょう。

標準ライブラリを利用すると重複する実装が減り、コードの記述量を大幅に削減できます。

正規表現モジュール
------------------

ここでは例として標準ライブラリの1つ ``re`` モジュールをimportして利用します。
``re`` モジュールはPythonで正規表現を扱うためのモジュールです。

``re.search()`` 関数を使って、文字列が正規表現にマッチするか調べられます。第1引数に正規表現、第2引数に対象の文字列を渡します（:numref:`re-module`）。

.. _re-module:

.. code-block:: python
    :caption: reモジュールの利用

    >>> import re
    >>> m = re.search('(P(yth|l)|Z)o[pn]e?', 'Python')
    >>> m
    <_sre.SRE_Match object; span=(0, 6), match='Python'>

正規表現にマッチした場合、 ``re.search()`` は結果を表すマッチオブジェクトを返します。
マッチオブジェクトから値を取り出すには、 ``.group()`` メソッドを呼び出します（:numref:`match-object`）。

.. _match-object:

.. code-block:: python
    :caption: 正規表現にマッチした文字列の取得

    >>> m.group()
    'Python'

正規表現がグループを含む場合、グループの番号を引数に渡して取り出せます。
引数を指定しないか、0を指定すると、正規表現全体のマッチが返されます（:numref:`match-group`）。

.. _match-group:

.. code-block:: python
    :caption: グループを指定して文字列の取得

    >>> m = re.search('py(thon)', 'python')
    >>> m.group()
    'python'
    >>> m.group(0)
    'python'
    >>> m.group(1)
    'thon'

正規表現にマッチしない場合は、:numref:`not-match` に示すように何も返しません（``None`` を返します）。

.. _not-match:

.. code-block:: python
    :caption: 正規表現にマッチしない場合

    >>> re.search('py', 'ruby')
    >>>

.. admonition:: コラム: 正規表現の文字列

    正規表現の文字列にはPythonのraw文字列を使うのが一般的です。

    ``r`` プレフィックスをつけてraw文字列を定義します。
    raw文字列ではバックスラッシュを特別扱いしないので、
    正規表現中にバックスラッシュを使う際に ``'\\'`` と書く必要がなくなります。

その他便利なモジュールについては、一部を「 :ref:`standard-library` 」で扱います。

``re`` モジュールには、ここで説明していない有効な使い方があります。
Pythonの公式ドキュメントの「 `reモジュール <http://docs.python.jp/3.5/library/re.html>`_ 」を参考にしてください。

また、他のPython標準ライブラリについては、「 `Python標準ライブラリ <http://docs.python.jp/3.5/library/index.html>`_ 」を参考にしてください。


まとめ
==========

本節では、Pythonでファイルを読み書きする方法、Pythonファイルを分割して再利用する方法を解説しました。
