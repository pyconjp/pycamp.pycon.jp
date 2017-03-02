==================================
スクレイピング
==================================

:節サブタイトル: 自動でデータを収集する方法

スクレイピングとは
==================
ウェブサイトから情報を抽出する、コンピュータソフトウェア技術のことをいいます。

Pythonを使って実行することができますので、これを機に習得してみましょう。


環境構築
=====================

前章の環境構築を参考にして、venvモジュールを利用して、新しい環境を構築してください。
その後、pipコマンドを実行し、スクレイピングに使用する requests と beautifulsoup4 を利用可能な状態にしてください。

.. code-block:: sh
   :caption: スクレイピング用の環境を構築

   $ mkdir scraping
   $ cd scraping
   $ python -m venv env
   $ source env/bin/activate
   (env) $ pip install requests
   (env) $ pip install beautifulsoup4

reuqestsとbeautifulsoup4
------------------------
スクレイピングを行うために2つのサードパーティ製パッケージをインストールしています。

`Requests <http://docs.python-requests.org/en/master/>`_ はウェブサイトにアクセスしてHTMLなどのデータを取得するためのライブラリです。
Pythonの標準ライブラリ `urllib.request <https://docs.python.jp/3/library/urllib.request.html>`_ でも同様のことは行なえますが、より便利な requests をここでは使用します。

`Beautiful Soup <https://www.crummy.com/software/BeautifulSoup/bs4/doc/>`_ はHTMLやXMLの中身を解析して、任意の情報を取得するためのライブラリです。
Pythonの標準ライブラリ `html.parser <https://docs.python.jp/3/library/html.parser.html>`_ でも同様のことは行なえますが、より便利なのでここでは使用します。
なお、beautifulsoupとbeautifulsoup4が存在しますが、新しい **beautifulsoup4** を使うようにしてください。

目的
=====================
* スクレイピングでPythonに関する新着ニュース情報を取得してみよう
* 取得した情報をコンソールに出力してみよう


シンプルなスクレイピングのコード
================================

下記コードをsimple.pyという名前で保存します。

.. code-block:: python
   :caption: simple.py

   import requests
   from bs4 import BeautifulSoup


   def main():
       url = 'https://www.python.org/blogs/'
       res = requests.get(url)
       soup = BeautifulSoup(res.content, 'html.parser')
       records = soup.select('.event-title')

       for record in records:
           print(record.text)


   if __name__ == '__main__':
       main()


.. admonition:: コラム: Pythonのコーディング規約「pep8」

    Pythonには `pep8（ペップエイト） <https://www.python.org/dev/peps/pep-0008/>`_ というコーディング規約があります。

    複数の人で開発する際、人によって書き方がバラバラだと非常に読みにくいコードになってしまうので、pep8のルールに従う習慣を身につけておくとよいでしょう。

    自分のコードがpep8のルールに従っているかは、 `pycodestyle <http://pep8.readthedocs.io/en/latest/index.html#>`_ というツールを使って検証できます。

    pycodestyleは ``pip install pycodestyle`` でインストールできます。

    上記の例 ``simple.py`` を検証するなら、 ``pycodestyle --first simple.py`` を実行します。


コードの説明
------------
TODO: コードの説明をもうちょい詳細に書く

.. code-block:: python
   :caption: BeautifulSoup利用例

   >>> from bs4 import BeautifulSoup
   >>> soup = BeautifulSoup('<div><h1 id="test">TEST</h1></div>', 'html.parser')
   >>> soup.select('div h1#test')[0].text
   >>>'TEST'

* ``if __name__ == '__main__':`` と書いた部分がコード実行時に呼び出されます。

実行してみよう
--------------
先程作成したvenv環境をactivateし、simple.pyを実行します。
すると、Pythonに関する新着ニュースをウェブサイトから取得して表示します。

.. code-block:: sh
   :caption: simple.py 実行例

   (env) $ python simple.py
   The first release candidate for Python 3.4
   Python 3.3.4 released
   EuroPython Call for Proposals
   Python 3.3.4 release candidate has been released
   Python 3.4.0 beta 3 has been released
   Python 3.4.0 beta 2 has been released
   (以下省略)

.. admonition:: コラム: Shebang（シェバン）

   頻繁に利用するプログラムであれば、実行を簡単にするShebang（シェバン）を使うと便利です。

   コードの先頭に ``#!/usr/bin/env python`` を入れて、 ``chmod +x simple.py`` でファイルに実行権限を与えておくと、以下のように ``simple.py`` の指定だけでプログラムを実行することができます。

   .. code-block:: sh
      :caption: simple.py 実行例(Shebangを使った場合)

      (env) $ ./simple.py
      (以下省略)

作り変えてみよう
================
Reqeusts や BeautifulSoup の動作を変えて、さまざまなWebページからさまざまな要素を取得できます。
以下にそれぞれのライブラリの簡単な使い方を載せます。それ以外にもいろいろな使用方法があるので、ドキュメントを参考にしていろいろ作り変えてみてください。

Requests の主な使い方
---------------------
ここでは Requests の主な使い方の例をいくつか載せます。
詳細については以下の公式ドキュメントを参照してください。

:公式ドキュメント: `Requests: HTTP for Humans <http://docs.python-requests.org/en/master/>`_

以下は認証つきのURLにアクセスして、結果を取得する例です。

.. code-block:: pycon
   :caption: requests の使用例

   >>> import requests
   >>> r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
   >>> r.status_code
   200
   >>> r.headers['content-type']
   'application/json; charset=utf8'
   >>> r.encoding
   'utf-8'
   >>> r.text
   u'{"type":"User"...'
   >>> r.json()
   {u'private_gists': 419, u'total_private_repos': 77, ...}

POST を行う場合は以下のように実行します。

.. code-block:: pycon
   :caption: requests で POST する例

   >>> data = {'key': 'value'} # POST するパラメーター
   >>> r = requests.post('http://httpbin.org/post', data=data)

GET に `?key1=value1&key2=value2` のようなパラメーター付きでアクセスする場合は以下のように書きます。

.. code-block:: pycon
   :caption: requests でパラメーター付で GET する例

   >>> payload = {'key1': 'value1', 'key2': 'value2'}
   >>> r = requests.get('http://httpbin.org/get', params=payload)
   print(r.url)
   http://httpbin.org/get?key2=value2&key1=value1
   >>> payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
   >>> r = requests.get('http://httpbin.org/get', params=payload)
   >>> print(r.url)
   http://httpbin.org/get?key1=value1&key2=value2&key2=value3

BeautifulSoup4 の主な使い方
---------------------------
ここでは BeautifulSoup4 の主な使い方の例をいくつか載せます。
詳細については以下の公式ドキュメントを参照してください。

:公式ドキュメント: `Beautiful Soup Documentation <https://www.crummy.com/software/BeautifulSoup/bs4/doc/>`_

.. code-block:: pycon
   :caption: BeautifulSoup4 の使用例

   >>> import requests
   >>> from bs4 import BeautifulSoup
   >>> r = requests.get('https://www.python.org/news/')
   >>> soup = BeautifulSoup(r.content, 'html.parser') # 取得したHTMLを解析
   >>> soup.title # titleタグの情報を取得
   <title>Python News | Python.org</title>
   >>> soup.title.name
   'title'
   >>> soup.title.string # titleタグの文字列を取得
   'Python News | Python.org'
   >>> soup.a
   <a href="#content" title="Skip to content">Skip to content</a>
   >>> len(soup.find_all('a')) # 全ての a タグを取得しt len() で件数を取得
   164

        url = 'https://www.python.org/news/'
        res = requests.get(url)
        soup = BeautifulSoup(res.content, 'html.parser')


また、 ``find()`` ``find_all()`` などでタグを探す場合には、タグの属性などを条件として指定できます。

.. code-block:: pycon
   :caption: find/find_all の使用例

   >>> len(soup.find_all('h1')) # 指定したタグを検索
   3
   >>> len(soup.find_all(['h1', 'h2', 'h3'])) # 複数のタグのいずれかにマッチ
   24
   >>> len(soup.find_all('div', {'class': 'pubdate'})) # <div class="pubdate"> にマッチ
   21

まとめ
==========
本節では、Pythonでスクレイピングをする方法を解説しました。

requestsとbeautifulsoup4を使いこなすことにより、さまざまなウェブサイトから情報を取得できるようになります。

ただし、ウェブサイトにスクレイピングのために短時間に大量にアクセスをすると迷惑となるので、そういうことがないように注意してください。

参考書籍
==========
Pythonでのスクレイピングについてもいくつか書籍が出てきます。

- `PythonによるWebスクレイピング <https://www.oreilly.co.jp/books/9784873117614/>`_
- `Pythonクローリング＆スクレイピング ―データ収集・解析のための実践開発ガイド <http://gihyo.jp/book/2017/978-4-7741-8367-1>`_
- `Pythonによるスクレイピング＆機械学習 開発テクニックBeautifulSoup、scikit-learn、TensorFlowを使ってみよう <http://www.socym.co.jp/book/1079>`_

次の一歩
============

スクレイピングの例の実行ができたら、以下の様な改造を自習してみください。

- 別のサイトから同様に情報を抜き出してみる　＞URL変更とCSSセレクタの変更
- RSS(XML)から必要な情報を抜き出してみる　＞パーサの変更
- 抜き出したものを、ファイルに保存してみる　＞別の章との組み合わせ
- ログインが必要なサイトにログインして情報を抜き出してみる　＞requestsの応用
- 抜き出したものを、HTMLに加工して、ファイルに保存、出力してみる　＞各種応用
