==================================
スクレイピング
==================================

:節サブタイトル: 自動でデータを収集する方法

スクレイピングとは
==================
ウェブサイトから情報を抽出する、コンピュータソフトウェア技術のことをいいます。

ここではPythonを使った実用的なプログラムの例として、スクレイピングを行います。


環境構築
=====================

前章の「 :ref:`about-venv` 」を参考に、venvモジュールを利用して、スクレイピング用のvenv環境を構築します。
venv環境をactivateコマンドで有効にし、スクレイピングに使用する requests と beautifulsoup4 をpipコマンドでインストールします。

.. code-block:: sh
   :caption: スクレイピング用のvenv環境を構築

   $ mkdir scraping
   $ cd scraping
   $ python -m venv env
   $ source env/bin/activate
   (env) $ pip install requests
   (env) $ pip install beautifulsoup4

Reuqests
--------
:URL: http://docs.python-requests.org/en/master/

Requests について簡単に紹介します。
Reqeusts はウェブサイトにアクセスしてHTMLなどのデータを取得するためのライブラリです。
Pythonの標準ライブラリ `urllib.request <https://docs.python.jp/3/library/urllib.request.html>`_ でも同様のことは行なえますが、より便利な Requests をここでは使用します。

Beautiful Soup
--------------
:URL: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

Beautiful Soup はHTMLやXMLの中身を解析して、任意の情報を取得するためのライブラリです。
Pythonの標準ライブラリ `html.parser <https://docs.python.jp/3/library/html.parser.html>`_ でも同様のことは行なえますが、より便利な Beautiful Soup をここでは使用します。
なお、beautifulsoupとbeautifulsoup4が存在しますが、新しい **beautifulsoup4** を使うようにしてください。

シンプルなスクレイピングのコード
================================
スクレイピングの例として、PyCon JP 2016のスポンサー一覧のページ(https://pycon.jp/2016/ja/sponsors/)からスポンサー名とURLの情報を抜き出します。

.. figure:: images/sponsor-list.png
   :width: 30%

   スポンサー一覧ページ

下記コードをsimple.pyという名前で保存します(:numref:`simple-py`)。

.. _simple-py:

.. code-block:: python
   :caption: simple.py

   import requests
   from bs4 import BeautifulSoup


   def main():
       url = 'https://pycon.jp/2016/ja/sponsors/'
       res = requests.get(url)
       content = res.content
       soup = BeautifulSoup(content, 'html.parser')
       sponsors = soup.find_all('div', class_='sponsor-content')
       for sponsor in sponsors:
           url = sponsor.h3.a['href']
           name = sponsor.h4.text
           print(name, url)


   if __name__ == '__main__':
       main()


このコードを実行すると、以下のようにスポンサー名とURLの一覧が取得できます(:numref:`exec-simple-py`)。

.. _exec-simple-py:

.. code-block:: bash
   :caption: スクレイピングを実行

   (env) $ python simple.py
   株式会社フンザ http://hunza.jp/
   MonotaRO https://www.monotaro.com/
   Gandi.net https://www.gandi.net/
   株式会社JX通信社 http://jxpress.net/
   Port https://www.theport.jp/
   株式会社HDE https://www.hde.co.jp/
   :

   
.. admonition:: コラム: Pythonのコーディング規約「pep8」

    Pythonには `pep8（ペップエイト） <https://www.python.org/dev/peps/pep-0008/>`_ というコーディング規約があります。
    チームで開発をする際、人によってプログラムコードの書き方がバラバラだと読みにくいコードになってしまいます。
    そのため、pep8のルールに従う習慣を身につけておくとよいでしょう。

    コードがpep8のルールに従っているかは、 `pycodestyle <http://pep8.readthedocs.io/en/latest/index.html#>`_ というツールで検証できます(以前はツールの名前もpep8でした)。

    pycodestyleは ``pip install pycodestyle`` でインストールして使用します。
    ``simple.py`` を検証するには、 ``pycodestyle simple.py`` を実行します。


コードの解説
------------
上記のコードがどういった内容なのかを解説します。

* 以下のコードはrequestsとbeautifulsoup4をimportして利用できるようにしています。

.. code-block:: python
   :caption: モジュールのimport

   import requests
   from bs4 import BeautifulSoup

* メインとなる処理を ``main`` 関数として定義しています。
  なお、関数の名前に特に決まりはなく、必ずしも ``main`` である必要はありません。

.. code-block:: python
   :caption: main()関数の定義

   def main():

* Requestsを使用して、Webページの内容(HTML)を取得します。res.contentにHTMLの中身が文字列データとして入っています。
 
.. code-block:: python
   :caption: ページの内容を取得

       url = 'https://pycon.jp/2016/ja/sponsors/'
       res = requests.get(url)
       content = res.content

* 次にHTMLをBeautiful Soupに渡して解析します。HTMLの解析についてはもう少し詳しく説明します。
       
.. code-block:: python
   :caption: WebページをBeautiful Soupで解析

       soup = BeautifulSoup(content, 'html.parser')
       sponsors = soup.find_all('div', class_='sponsor-content')
       for sponsor in sponsors:
           url = sponsor.h3.a['href']
           name = sponsor.h4.text
           print(name, url)


* 最後に、このスクリプトが実行された時に、main()関数を実行するように指定します。
       
.. code-block:: python
   :caption: main()関数を実行

   if __name__ == '__main__':
       main()

HTMLの解析の解説
----------------
Beautiful SoupでHTMLを解析して、値が取り出せましたが、どのように指定しているのでしょうか?
スポンサー一覧のHTMLを見てみると、以下のような形式になっています。(:numref:`sponsor-list-html`)

.. _sponsor-list-html:

.. code-block:: html
   :caption: スポンサー一覧のHTML

   <div class="span12">
     <h2>Diamond</h2>
     <div class="row">
       <div class="span4">
         <div class="sponsor" id="sponsor-10">
           <div class="sponsor-content">
             <h3>
               <a href="http://hunza.jp/">
                 <img src="/2016/site_media/media/sponsor_files/Hunza_logo.png.150x80_q85.png" alt="株式会社フンザ" />
               </a>
             </h3>
             <h4>株式会社フンザ</h4>
             <p><a href="http://hunza.jp/">http://hunza.jp/</a></p>
             <p><p>フンザは「世の中の文化となるウェブサービスを創る」をビジョンに、国内No.1のC2Cチケット売買サイト「チケットキャンプ」を開発/運営しています。</p></p>
           </div>
         </div>
       </div>
     </div>
   </div>
   <div class="span12">
     <h2>Platinum</h2>
       <div class="row">
         <div class="span4">
           <div class="sponsor" id="sponsor-4">
             <div class="sponsor-content">
               <h3>
                 <a href="https://www.monotaro.com/">
                   <img src="/2016/site_media/media/sponsor_files/logo-PyCon.png.150x80_q85.jpg" alt="MonotaRO" />
                 </a>
               </h3>
               <h4>MonotaRO</h4>
               <p><a href="https://www.monotaro.com/">https://www.monotaro.com/</a></p>
               <p><p>「ITで、間接資材調達を変革する」<br />モノタロウは、働く現場で必要となる様々な間接資材(最終製品となる原材料を除く全ての資材)約900万点をインターネットで販売しています。<br />様々な現場のニーズにお応えすべく、自社開発の高度な検索システムと精緻なデータベースマーケティングが実現する「お客様ごとの最適化したレコメンドサービス」で、従来の非効率的な間接資材調達を変革し、社会に新しい価値を提供しています。</p></p>
   (以下続く)

このHTMLを見ると、スポンサーの名前とURLは以下のようにして取得できそうです。

* 一つのスポンサーの情報は ``<div class="sponsor-content">`` の中に入っている
* スポンサーのURLは ``<h3>`` タグの中の ``<a>`` タグの ``href`` アトリビュートに入っている
* スポンサー名は ``<h4>`` タグで囲まれた中に入っている

HTMLの構造がわかったところで、もう一度HTMLを解析しているコードを見てみます。

.. code-block:: python
   :caption: WebページをBeautiful Soupで解析

       soup = BeautifulSoup(content, 'html.parser')
       sponsors = soup.find_all('div', class_='sponsor-content')
       for sponsor in sponsors:
           url = sponsor.h3.a['href']
           name = sponsor.h4.text
           print(name, url)

まず、 ``soup.find_all()`` メソッドで、全スポンサーの情報が含まれている div 要素を取得しています。
次に、各スポンサー情報(sponsor変数に入っている)から値を取り出しています。
最初にURLを取得して、次にスポンサー名を取得しています。

作り変えてみよう
================
Reqeusts や Beautiful Soup の動作を変えて、さまざまなWebページから色んな要素を取得できます。

以下にそれぞれのライブラリの簡単な使い方を紹介します。それ以外にもいろいろな使用方法があるので、ドキュメントを参考にしていろいろ作り変えてみてください。

Requests の主な使い方
---------------------
ここでは Requests の主な使い方の例をいくつか載せます。
詳細については以下の公式ドキュメントを参照してください。

:公式ドキュメント: `Requests: HTTP for Humans <http://docs.python-requests.org/en/master/>`_

以下は認証つきのURLにアクセスして、結果を取得する例です。

.. code-block:: pycon
   :caption: 認証付きURLにアクセスする

   >>> import requests
   >>> r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
   >>> r.status_code
   200

POST を行う場合は以下のように、POSTのパラメーターを辞書で定義します。

.. code-block:: pycon
   :caption: requests で POST する

   >>> payload = {'key1': 'value1', 'key2': 'value2'} # POST するパラメーター
   >>> r = requests.post('http://httpbin.org/post', data=payload)
   >>> print(r.text)

GET に ``?key1=value1&key2=value2`` のようなパラメーター付きでアクセスする場合も同様に、辞書で定義します。

.. code-block:: pycon
   :caption: requests でパラメーター付で GET する

   >>> payload = {'key1': 'value1', 'key2': 'value2'}
   >>> r = requests.get('http://httpbin.org/get', params=payload)
   >>> print(r.url)
   http://httpbin.org/get?key2=value2&key1=value1
   >>> payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
   >>> r = requests.get('http://httpbin.org/get', params=payload)
   >>> print(r.url)
   http://httpbin.org/get?key1=value1&key2=value2&key2=value3

Beautiful Soup の主な使い方
---------------------------
ここでは Beautiful Soup の主な使い方の例をいくつか載せます。
詳細については以下の公式ドキュメントを参照してください。

:公式ドキュメント: `Beautiful Soup Documentation <https://www.crummy.com/software/BeautifulSoup/bs4/doc/>`_

.. code-block:: pycon
   :caption: Beautiful Soup の使用例

   >>> import requests
   >>> from bs4 import BeautifulSoup
   >>> r = requests.get('https://www.python.org/blogs/')
   >>> soup = BeautifulSoup(r.content, 'html.parser') # 取得したHTMLを解析
   >>> soup.title # titleタグの情報を取得
   <title>Our Blogs | Python.org</title>
   >>> soup.title.name
   'title'
   >>> soup.title.string # titleタグの文字列を取得
   'Our Blogs | Python.org'
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
   >>> len(soup.find_all('h3', {'class': 'event-title'})) # <h3 class="event-title"> にマッチ
   5

まとめ
==========
本節では、Pythonでスクレイピングをする方法を解説しました。

RequestsとBeautiful Soupを使いこなすことにより、さまざまなウェブサイトから情報を取得できるようになります。

なお、短時間にWebサイトに大量にアクセスをすると迷惑となるので、そういうことがないようにプログラムを実行するときには注意してください。

参考書籍
==========
Pythonでのスクレイピングについてもいくつか書籍が出ています。

- `PythonによるWebスクレイピング <https://www.oreilly.co.jp/books/9784873117614/>`_
- `Pythonクローリング＆スクレイピング ―データ収集・解析のための実践開発ガイド <http://gihyo.jp/book/2017/978-4-7741-8367-1>`_
- `Pythonによるスクレイピング＆機械学習 開発テクニックBeautifulSoup、scikit-learn、TensorFlowを使ってみよう <http://www.socym.co.jp/book/1079>`_
