.. _guide-intro:

=============================
Pythonをはじめよう
=============================

:節サブタイトル: Pythonのインストール方法、実践を通したPythonの特徴と基本の紹介

Pythonをはじめましょう！

本節ではPythonのインストール方法、Pythonの特徴と基本を紹介します。
ただ紹介するだけではなく、簡単なプログラムを実装しつつ実践的に学んでいきます。

Pythonを学ぶうえで役に立つWebの情報、書籍も紹介します。

.. _python-install:

Pythonのインストール
====================

ここではPythonのインストール方法を説明します。

Linux、OS X、Windows の3 つの環境でのインストール手順を説明します。

Linux (Ubuntu Server) での場合
-------------------------------------

本書では、動作環境 `Ubuntu Server 14.04 <https://wiki.ubuntu.com/TrustyTahr/ReleaseNotes>`_ 、
Pythonは2系の最新版2.7.9を想定しています。

Ubuntu 14.04では標準でPython 2.7.6がインストールされています。

ですので、 2.7.9 をインストールする方法を説明します。

ソースビルドでのインストール
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ubuntu 14.04にソースコードからPython 2.7.9をインストールします（:numref:`package-install`）。

まずパッケージ全体をアップグレードし、Pythonによる開発で必要になるパッケージをインストールします。

.. _package-install:

.. code-block:: bash
    :caption: パッケージの更新と必要なパッケージのインストール

    $ sudo apt-get -y update
    $ sudo apt-get -y upgrade
    $ sudo apt-get -y install build-essential
    $ sudo apt-get -y install libsqlite3-dev
    $ sudo apt-get -y install libreadline6-dev
    $ sudo apt-get -y install libgdbm-dev
    $ sudo apt-get -y install zlib1g-dev
    $ sudo apt-get -y install libbz2-dev
    $ sudo apt-get -y install sqlite3
    $ sudo apt-get -y install tk-dev
    $ sudo apt-get -y install zip
    $ sudo apt-get -y install libssl-dev
    $ sudo apt-get -y install gfortran
    $ sudo apt-get -y install liblapack-dev

.. g++はbuild-essentialsで、opensslは標準で入る。

Pythonのソースコードをビルドし、インストールします（:numref:`python-build`）。

.. _python-build:

.. code-block:: bash
    :caption: Python 2.7.9のソースからのインストール

    $ wget https://www.python.org/ftp/python/2.7.9/Python-2.7.9.tgz
    $ tar axvf ./Python-2.7.9.tgz
    $ cd ./Python-2.7.9/
    $ LDFLAGS="-L/usr/lib/x86_64-linux-gnu" ./configure --with-ensurepip
    $ make
    $ sudo make install

インストールが完了したらPythonのバージョンが2.7.9になっていることを確認します。

インストール直後は、 ``hash -r`` を実行してコマンドのパスを再読み込みします（:numref:`check-version`）。

.. _check-version:

.. code-block:: bash
    :caption: Pythonのバージョン確認

    $ hash -r
    $ python -V
    Python 2.7.9

.. admonition:: コラム: インストール先の指定


   ソースコードのビルドで ``configure`` を実行する際に、 ``--prefix`` オプションを付けるとインストール先のディレクトリを指定できます。

   /opt/python2.7.9 ディレクトリ以下にインストールするには、次のように指定します

    .. code-block:: python
        :caption: prefixオプション付きconfigure

        LDFLAGS="-L/usr/lib/x86_64-linux-gnu" ./configure --prefix=/opt/python2.7.9 --with-ensurepip

OS Xでの場合
-------------------------------------
OS XでPythonを利用する場合は、Pythonの公式サイトで配布されているビルド済みのパッケージをインストールします。

次のページで「Latest Python 2 Release - Python 2.7.9」をクリックすると詳細画面に移動します。64 ビット版（Mac OS X 64-bit/32-bit installer）または32 ビット版（Mac OS X 32-bit i386/PPC installer）をダウンロードしてインストールします。

- `Python Releases for Mac OS X <https://www.python.org/downloads/mac-osx/>`_ 

詳しくはPythonの公式ドキュメントの「 `MacintoshでPythonを使う <http://docs.python.jp/2/using/mac.html>`_ 」を参考にしてください。

Windowsでの場合
-------------------------------------

WindowsでPythonを利用する場合は、Pythonの公式サイトで配布されているWindowsインストーラを利用します。

次のページで「Latest Python 2 Release - Python 2.7.9」をクリックすると詳細画面に移動します。64ビット版（Windows x86-64 MSI Installer）または32 ビット版（Windows x86 MSI Installer）をダウンロードし、ウィザードに従ってインストールします（:numref:`windows-install`）。

- `Python Releases for Windows <https://www.python.org/downloads/windows/>`_

.. _windows-install:

.. figure:: images/pythonforwindows1.png
   :width: 400

   Python for Windowsのインストール画面

pathの設定
^^^^^^^^^^^^^^^^^^^^^

コマンドプロンプトなどから ``python`` と打ち込んだだけでプログラムを実行できるようにするため、環境変数pathの設定を行います。

コントロールパネルを開き、［システムとセキュリティ］→［システム］→［システムの詳細設定］をクリックすると、［システムのプロパティ］が表示されます。

［詳細設定］タブの［環境変数］ボタンをクリックし、［ユーザー環境変数］の「PATH」に、 ``C:¥Python27¥;C:¥Python27¥Scripts;`` という値を新規追加します。

.. _enjoy-python:

Pythonを楽しもう
=====================

Pythonのインストールはできましたか？

ここではPythonの基本の基本を紹介します。

ただ紹介するだけではなく、「FizzBuzz」という簡単なプログラム（詳細は後述）を実装できることを目的にします。

Pythonについてより詳しくは、後述の節で説明します。

Pythonインタープリタ
------------------------

さっそくPythonで遊んでみましょう。

シェルまたはコマンドプロンプトで ``python`` と入力し、Pythonインタープリタを対話モードで起動しましょう（:numref:`python-interpreter`）。

.. _python-interpreter:

.. code-block:: bash
    :caption: Pythonインタープリタの起動

    $ python
    Python 2.7.9 (default, Dec 29 2014, 17:03:36)
    [GCC 4.8.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

初めにPythonインタープリタの情報と、大なり記号3つ（``>>>``）が表示されます。

これがPythonのプロンプトです。終了するにはCtrl-Dを入力します（WindowsではCtrl-Z）。

Pythonを電卓にする
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

電卓のようにPythonを使ってみましょう（:numref:`python-calc`）。

.. _python-calc:

.. code-block:: python
    :caption: 四則演算と代入

    >>> 2 + 2
    4
    >>> 3 - 8
    -5
    >>> 6 * 9
    54
    >>> 8 / 2
    4
    >>> 5 % 2
    1
    >>> width = 60
    >>> height = 90
    >>> width * height
    5400

初めの4つは整数型（int）での四則演算（``+``、``-``、``*``、``/``）と剰余（``%``）です。

次に等号（``=``）を使って値を代入しています。

``width`` 、 ``height`` という変数を作成し、2つを掛け合わせています。

文字列
---------------

数字だけを扱うなら卓上電卓で十分ですね。文字列型（str）を使ってみましょう。

:numref:`string-type` のように、シングルクォート（``'``）かダブルクォート（``"``）の間に文字を入力することで、文字列を定義します。

.. _string-type:

.. code-block:: python
    :caption: 文字列型

    >>> 'Hello,world'
    'Hello,world'
    >>> "Monty Python's Flying Circus"
    "Monty Python's Flying Circus"

文字列中にシングルクォートを含む場合はダブルクォートを使います
（ :ref:`types-str` で説明する文字のエスケープも使えます）。

文字列は順序を持つシーケンス型の1つです。

.. admonition:: コラム: シーケンス型

   シーケンス型は順序を持つ型で、Python標準では7つの型があります。

   シーケンス型の詳細はPythonの公式ドキュメントを参照してください。

   * シーケンス型 http://docs.python.jp/2/library/stdtypes.html#typesseq

リスト
-----------------

リスト（list）は、複数のデータ型の入れ物として使えます（:numref:`list`）。

.. _list:

.. code-block:: python
    :caption: リスト

    >>> ['Hello', 3]
    ['Hello', 3]

リストも文字列と同じで、順序を持つシーケンス型の1つです。

複数のデータ型と組み合わせて使えるコレクションの1つでもあります。

関数
-------------

関数は、 ``def`` を使って定義します。

.. code-block:: python

   def ＜関数名＞(＜引数の変数名＞):

と書きます。末尾にはコロン（``:``）が必要です。

値を返すには、 ``return`` を使います。引数を2つ受け取り、合計値を返す関数は :numref:`function-def` になります。

.. _function-def:

.. code-block:: python
    :caption: 関数定義と呼び出し

    >>> def add(a, b):
    ...     return a + b
    ...
    >>> add(1, 3)
    4

Python はブロック構造をインデント（通常は4つのスペース）で書きます。

C言語のように波括弧（``{ }``）で囲む必要はなく、インデント自体が文の構造となります。

``add()`` 関数内の1行目のreturn文は関数の中身なので、インデントで字下げします。

関数を書き終わったときにも改行を入力してください（最後の入力が文として終了していない場合、プロンプトが3つのドット（``...``）になります）。

関数を呼び出すには関数名に括弧（``( )``）を付けて実行します。

:numref:`function-def` のように引数がある場合は、括弧内に引数を渡します。1と3を足した値、4が返されています。

組み込み関数
^^^^^^^^^^^^^^^^^^^^^

Pythonには標準でいくつか関数が提供されています。これを組み込み関数と呼びます。

たとえば、指定された整数のリストを作成する ``range()`` 関数は、 :numref:`range` のように使います。

.. _range:

.. code-block:: python
    :caption: 組み込み関数range

    >>> range(10)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

組み込み関数の一覧は、次のドキュメントを参照してください。

* 組み込み関数 http://docs.python.jp/2/library/functions.html

FizzBuzz
=====================

ここで「FizzBuzz」というゲームを解くプログラムをPythonで書いてみましょう。

FizzBuzzとは、複数の人が集まって行うゲームです。

ひとりひとりが1から順に数字を発言し、数字が3で割り切れる場合は「Fizz」、5で割り切れる場合は「Buzz」、3 と5 で割り切れる場合は「FizzBuzz」と発言するゲームです。

1から15までの答えを並べると次のようになります。

.. code-block:: none
    :caption: FizzBuzzの15までの回答

    1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz

1から100までのFizzBuzzを表示する処理を作りましょう。

FizzBuzzは簡単な問題ですが、実装する言語の制御文を使いこなす必要があり、言語入門の第一歩としてちょうどよい題材です

.. FizzBuzz Question/Test について書くかどうか http://blog.codinghorror.com/why-cant-programmers-program/_

Pythonファイル
----------------------

Pythonファイルを作成しFizzBuzzを実装していきましょう。

今まではPythonインタープリタ上で直接処理を実行していましたが、少し長い処理を書くには不便です。

Python インタープリタの対話モードを終了し（【Ctrl】＋【D】を押下し）、fizzbuzz.py というファイルを作成します。

:numref:`fizzbuzz-1` のように書きます。

.. _fizzbuzz-1:

.. code-block:: python
    :caption: fizzbuzz.py

    def fizzbuzz(num):
        return num

    print fizzbuzz(4)


この ``fizzbuzz()`` 関数はなにも処理をせず引数をそのまま返します。これから処理を追加していくので安心してください。

``print`` 文を使っているのは実行結果を表示するためです。

対話モードでは、変数の値や関数の戻り値を変数に代入しない場合に、自動的に値を表示してくれました。

Python ファイルを作成して実行する場合は、 ``print`` 文が必要です。

``fizzbuzz.py`` を実行するには、 ``python`` コマンドに引数として渡します（:numref:`exec-fizzbuzz`）。

.. _exec-fizzbuzz:

.. code-block:: bash
    :caption: fizzbuzz.pyの実行

    $ python fizzbuzz.py
    4

for文
----------------

「1から100までのFizzBuzzを表示する」ために ``fizzbuzz()`` 関数に1から100まで順に値を与えます。

``for`` 文を使って繰り返し処理を実装しましょう（:numref:`for`）。

.. _for:

.. code-block:: python
    :caption: for文と関数の実行

    def fizzbuzz(num):
        return num

    for num in range(1, 101):
        print fizzbuzz(num)


.. _fizzbuzz-2:

.. code-block:: bash
    :caption: fizzbuzz.pyの実行(2)

    $ python fizzbuzz.py
    1
    2
    3
    .
    .
    100

:numref:`fizzbuzz-2` のように、実行すると1から100までの数字が表示されます。
``fizzbuzz()`` 関数には1 から100までの数字が順に与えられています。

現時点のfizzbuzz()関数は与えられた引数をそのまま返す実装なので、これで問題ありません。

for文は次のように書きます。

.. code-block:: python

   for ＜変数名＞ in ＜シーケンス＞:

``＜変数名＞`` にはループ内で繰り返される変数名、 ``＜シーケンス＞`` には繰り返しのための変数（シーケンス型のオブジェクト）を書きます。

:numref:`for` では、繰り返される変数 ``num`` が ``fizzbuzz()`` 関数に渡されています。

繰り返しのための変数は ``range(1, 101)`` の実行結果（1から100までのリスト）です。

``range()`` 関数の結果リストが返され、ひとつひとつの数字が繰り返し用の変数（``num``）に渡され、 ``for`` のブロックが実行されます

if文
----------------

FizzBuzzの処理を作るには、引数の数字（``num``）に応じて処理を分岐する必要があります。

処理の流れとしては次のようになります。

1. 引数 ``num`` を受け取る
2. ``num`` と3の剰余が0（3で割り切れる）、かつ ``num`` と5の剰余が0である（5で割り切れる）場合に、 ``'FizzBuzz'`` を返す
3. ``num`` と3の剰余が0の場合に、 ``'Fizz'`` を返す
4. ``num`` と5の剰余が0の場合に、 ``'Buzz'`` を返す
5. 2〜4のどれでもない場合、引数 ``num`` を文字列にして返す

Pythonで条件による処理の分岐を扱うにはif文を使います。

``fizzbuzz()`` 関数は、 :numref:`if` のようになります。

.. _if:

.. code-block:: python
    :caption: fizzbuzz関数を完成させる

    def fizzbuzz(num):
        if num % 3 == 0 and num % 5 == 0:
            return 'FizzBuzz'
        elif num % 3 == 0:
            return 'Fizz'
        elif num % 5 == 0:
            return 'Buzz'
        else:
            return str(num)

紹介していない要素がいくつか登場しています。

``if`` 文
^^^^^^^^^

``if`` 文は、条件に与えられた式が真と評価できる場合に、 ``if`` ブロックの処理を実行します。

``elif`` 文は、 ``if`` 文の条件が偽の場合に、追加の条件を与えます。追加の条件が真の場合に、 ``elif`` ブロックの処理を実行します。

``else`` ブロックは、どの条件にも当てはまらない場合に実行されます。

演算子
^^^^^^
``==`` は比較演算子の1つで、左辺と右辺が値が同じ場合に真（``True``） を返します。それ以外の場合には偽（``False``）を返します。

``and`` はブール演算子の1つで、左右の条件が ``True`` の場合に ``True`` を返します（より正確には、左の条件が真と評価できる場合に右を評価して結果を返します）。

``str()`` 関数
^^^^^^^^^^^^^^

引数を文字列に変換して返します。

FizzBuzz処理の実装の完了
------------------------

これで ``fizzbuzz()`` 関数の実装が完了しました。

``fizzbuzz.py`` を実行しましょう。 :numref:`fizzbuzz-out` のような結果になります。

.. _fizzbuzz-out:

.. code-block:: bash
    :caption: 完成したfizzbuzz.pyの実行

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

おめでとうございます！ これがPythonの第一歩です。

FizzBuzz はいろいろな方法で実装できます。もっと短く、わかりやすく書くにはどうすればよいか、チャレンジしてみてください。

Webや書籍の情報
=======================

最後に、Pythonの学習の参考になるWebや書籍の情報を紹介します。

Web
------

Python 2.7

- Python 2.7 チュートリアル http://docs.python.jp/2/tutorial/
- Python HOWTO http://docs.python.jp/2/howto/

Python 3.4

- Python 3.4 チュートリアル http://docs.python.jp/3.4/tutorial/
- Dive into Python 3 日本語版 http://diveintopython3-ja.rdy.jp/
- Python HOWTO http://docs.python.jp/3.4/howto/

書籍
--------

- 『初めてのPython 第3版』（Mark Lutz著、夏目大訳、2009年、オライリージャパン、ISBN978-4-8731-1393-7）
- 『Pythonスタートブック』（辻真吾著、2010年、技術評論社、ISBN978-4-7741-4229-6）
- 『パーフェクトPython』（Pythonサポーターズ著、2013年、技術評論社、ISBN978-4-7741-5539-5）
- 『エキスパートPythonプログラミング』（TarekZiade著、稲田直哉、渋川よしき、清水川貴之、森本哲也訳、2010年、アスキーメディアワークス、ISBN978-4-0486-8629-7）

その他
------
Pythonの基礎力を上げるには、次のサイトもオススメです。プログラムで解く数学の問題集で、Webから無料で挑戦できます。

- `ProjectEuler <https://projecteuler.net/>`_

まとめ
=============
本節では、Python のインストール方法、FizzBuzzを通じたPythonの特徴、基本、役立つ
Web の情報、書籍を紹介しました。次節では、Pythonの基本のデータ型について説明します。
