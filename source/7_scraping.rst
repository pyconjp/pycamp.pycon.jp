==================================
スクレイピング
==================================

:節サブタイトル: 自動でデータを収集する方法

そもそもスクレイピングとは
==========================
ウェブサイトから情報を抽出する、コンピュータソフトウェア技術のことをいいます。

Pythonを使って実行することができますので、これを機に習得してみましょう。


環境構築
=====================

前章の環境構築を参考にして、pyvenvを実行し、新しい環境を構築してください。
その後、pipコマンドを実行し、スクレイピングに使用する requests と beautifulsoup4 を利用可能な状態にしてください。

.. code-block:: sh

   $ mkdir scraping
   $ cd scraping
   $ pyvenv env
   $ source env/bin/activate
   (env) $ pip install requests
   (env) $ pip install beautifulsoup4

目的
=====================
#. スクレイピングでPythonに関する新着ニュース情報を取得してみよう
#. 取得した情報をコンソールに出力してみよう


実際のコード
=====================

下記コードをsimple.pyという名前で保存してみましょう

.. code-block:: python

    #! /usr/bin/env python
    import requests
    from bs4 import BeautifulSoup


    def main():
        url = 'https://www.python.org/news/'
        res = requests.get(url)
        soup = BeautifulSoup(res.content, 'html.parser')
        records = soup.select('h2.news')
        iter_records = iter(records)

        for record in iter_records:
            print(record.text)

    if __name__ == '__main__':
        main()


コードの説明
------------
* 「#! /usr/bin/env python」って何？
    Pythonを簡単に実行するためのおまじないのようなものです。
    詳しくはShebang(シェバン)といいます。

* 「BeautifulSoup」って何？
    HTMLを解析するライブラリになります。

.. code-block:: python
    :caption: BeautifulSoup利用例

    >>> from bs4 import BeautifulSoup
    >>> soup = BeautifulSoup('<div><h1 id="test">TEST</h1></div>', 'html')
    >>> soup.select_one('div h1#test').text
    >>>'TEST'

* ``if __name__ == '__main__':`` と書いた部分がコード実行時に呼び出されます。

実行してみよう
==============
作成した環境にactivateした後、下記のコマンドを実行してみましょう

.. code-block:: python

   (env) $ python simple.py
   The first release candidate for Python 3.4
   Python 3.3.4 released
   EuroPython Call for Proposals
   Python 3.3.4 release candidate has been released
   Python 3.4.0 beta 3 has been released
   Python 3.4.0 beta 2 has been released
   (以下省略)

実行すると、Pythonに関する新着ニュースが表示されることが確認できます。

作り変えてみよう
================
Reqeusts や BeautifulSoup の動作を変えて、さまざまなWebページからさまざまな要素を取得できます。
以下に簡単なライブラリの使い方を載せます。それ以外にもいろいろな使用方法があるので、ドキュメントを参考にしてください。

requests の主なメソッド
-----------------------
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

- 公式ドキュメント: `Requests: HTTP for Humans — Requests 2.10.0 documentation <http://docs.python-requests.org/en/master/>`_

beautifulsoup4 の主なメソッド
-----------------------------

.. code-block:: python

- 公式ドキュメント: `Beautiful Soup Documentation <https://www.crummy.com/software/BeautifulSoup/bs4/doc/>`_


まとめ
==========
本節では、Pythonでスクレイピングをする方法を解説しました。

自動化することにより、作業を効率化することができます。

目的に応じて処理を記述していきましょう。


参考
==========
- wikipedia(スクレイピング) https://ja.wikipedia.org/wiki/ウェブスクレイピング
- wikipedia(pip) https://ja.wikipedia.org/wiki/Pip
- `Requests: HTTP for Humans — Requests 2.10.0 documentation <http://docs.python-requests.org/en/master/>`_
- `Beautiful Soup Documentation <https://www.crummy.com/software/BeautifulSoup/bs4/doc/>`_

