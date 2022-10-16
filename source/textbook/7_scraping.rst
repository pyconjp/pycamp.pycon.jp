.. index:: Scraping

=========================
 Web API、スクレイピング
=========================

:節サブタイトル: 自動でデータを収集する方法

Web APIとスクレイピングとは
===========================
**Web API** はインターネット上に用意されているAPIをプログラムから呼び出す技術のことです。
**スクレイピング** はウェブサイトから情報を抽出する、コンピュータソフトウェア技術のことをいいます。

ここではPythonを使った実用的なプログラムの例として、Web APIとスクレイピングの演習を行います。


環境構築
========

前章の「 :ref:`about-venv` 」を参考に、venvモジュールを利用して、スクレイピング用のvenv環境を構築します。
venv環境を ``activate`` コマンドで有効にし、Web APIとスクレイピングに使用する **Requests** と **Beautiful Soup 4** を ``pip`` コマンドでインストールします。

.. code-block:: sh
   :caption: 演習用のvenv環境を構築(macOS、Linux)

   $ mkdir scraping
   $ cd scraping
   $ python3 -m venv env
   $ source env/bin/activate
   (env) $ pip install requests
   (env) $ pip install beautifulsoup4

.. code-block:: sh
   :caption: 演習用のvenv環境を構築(Windows)

   > mkdir scraping
   > cd scraping
   > python -m venv env
   > env\Scripts\Activate.ps1
   (env) > pip install requests
   (env) > pip install beautifulsoup4

.. index:: Requests

Requests
--------
:URL: https://requests.readthedocs.io/

Requests について簡単に紹介します。
Requests はウェブサイトにアクセスしてHTMLなどのデータを取得するためのライブラリです。
Pythonの標準ライブラリ `urllib.request <https://docs.python.org/ja/3/library/urllib.request.html>`_ でも同様のことは行なえますが、より便利な Requests をここでは使用します。

.. index:: Beautiful Soup 4

Beautiful Soup 4
----------------
:URL: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

Beautiful Soup 4はHTMLやXMLの中身を解析して、任意の情報を取得するためのライブラリです。
Pythonの標準ライブラリ `html.parser <https://docs.python.org/ja/3/library/html.parser.html>`_ でも同様のことは行なえますが、より便利な Beautiful Soup 4 をここでは使用します。
なお、beautifulsoupとbeautifulsoup4が存在しますが、新しい **beautifulsoup4** を使うようにしてください。

シンプルなWeb APIのコード
=========================
Web APIの例としてconnpassのAPIを実行して、pythonというキーワードを含んだ2018年12月に開催されるイベント情報を取得します。

* `APIリファレンス - connpass <https://connpass.com/about/api/>`_

下記のコードを ``events.py`` という名前で保存します(:numref:`events-py`)。

.. _events-py:

.. code-block:: python
   :caption: events.py

   import requests


   def main():
       params = {
           'keyword': 'python',
           'ym': '201812',
       }
       url = 'https://connpass.com/api/v1/event/'
       r = requests.get(url, params=params)
       event_info = r.json()  # レスポンスのJSONを変換

       print('件数:', event_info['results_returned'])  # 件数を表示
       for event in event_info['events']:
           print(event['title'])
           print(event['started_at'])

   if __name__ == '__main__':
       main()
           
このコードを実行すると、以下のようにイベントタイトルと日付の一覧が取得できます(:numref:`exec-events-py`)。

.. _exec-events-py:

.. code-block:: bash
   :caption: connpass APIを実行

   (env) $ python events.py
   件数: 10
   【超初心者対象】プログラミング未経験者が初心者になるためのPython体験@池袋
   2018-11-28T19:00:00+09:00
   【初心者歓迎】大阪Python もくもく会 #1
   2018-11-16T19:00:00+09:00
   [R]『Ｒ統計解析パーフェクトマスター』１冊丸ごと演習会
   2018-11-23T14:00:00+09:00
   :

コードの解説
------------
上記のコードがどういった内容なのかを解説します。

* Web APIを実行するために ``requests`` をインポートします

.. code-block:: python
   :caption: モジュールのインポート

   import requests

* メインとなる処理を ``main`` 関数として定義しています。 なお、関数の名前に特に決まりはなく、必ずしも ``main`` である必要はありません。

.. code-block:: python
   :caption: main()関数の定義

   def main():

* APIのパラメーターとしてキーワードに ``python`` を、範囲に ``201812`` を指定します。パラメーターを書き換えれば検索条件が変わります。

.. code-block:: python
   :caption: パラメーターを作成

       params = {
           'keyword': 'python',
           'ym': '201812',
       }

* ``requests.get()`` にURLとパラメーターを指定して結果を取得します。
* 結果はJSON形式で返ってくるので、 ``.json()`` メソッドでPythonのデータ型（辞書、リスト等）に変換します。

.. code-block:: python
   :caption: Web APIを実行して結果を取得

       url = 'https://connpass.com/api/v1/event/'
       r = requests.get(url, params=params)
       event_info = r.json()  # レスポンスのJSONを変換

* Pythonデータ型のイベント情報から、件数とイベント名、開催日を取得して出力します。

.. code-block:: python
   :caption: 件数とイベント名、開催日を出力

       print('件数:', event_info['results_returned'])  # 件数を表示
       for event in event_info['events']:
           print(event['title'])
           print(event['started_at'])

* 最後に、このスクリプトが実行された時に、main()関数を実行するように指定します。

.. code-block:: python
   :caption: main()関数を実行

   if __name__ == '__main__':
       main()
   
シンプルなスクレイピングのコード
================================
スクレイピングの例として、PyCon JP 2017のスポンサー一覧のページ(https://pycon.jp/2017/ja/sponsors/)からスポンサー名とURLの情報を抜き出します。

.. figure:: images/sponsor-list.png
   :width: 30%

   スポンサー一覧ページ

下記コードを ``simple.py`` という名前で保存します(:numref:`simple-py`)。

.. _simple-py:

.. code-block:: python
   :caption: simple.py

   import requests
   from bs4 import BeautifulSoup


   def main():
       url = 'https://pycon.jp/2017/ja/sponsors/'
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
   株式会社SQUEEZE https://squeeze-inc.co.jp/
   株式会社MonotaRO https://recruit.monotaro.com/?utm_medium=outside_flier&utm_source=pycon.jp&utm_campaign=PyConJP2017
   LINE株式会社 https://engineering.linecorp.com/
   Retty株式会社 http://corp.retty.me/
   iRidge, Inc. https://iridge.jp/
   株式会社いい生活 http://www.e-seikatsu.info/recruit/graduate/
   :

.. index:: PEP8

.. admonition:: コラム: Pythonのコーディング規約「PEP8」

    Pythonには `PEP8（ペップエイト） <https://www.python.org/dev/peps/pep-0008/>`_ というコーディング規約があります。
    チームで開発をする際、人によってプログラムコードの書き方がバラバラだと読みにくいコードになってしまいます。
    そのため、PEP8のルールに従う習慣を身につけておくとよいでしょう。

    コードがPEP8のルールに従っているかは、 `pycodestyle <http://pep8.readthedocs.io/en/latest/index.html#>`_ というツールで検証できます(以前はツールの名前もpep8でした)。

    pycodestyleは ``pip install pycodestyle`` でインストールして使用します。
    ``simple.py`` を検証するには、 ``pycodestyle simple.py`` を実行します。


コードの解説
------------
上記のコードがどういった内容なのかを解説します。

* 以下のコードはRequestsとBeautiful Soup 4をimportして利用できるようにしています。

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

       url = 'https://pycon.jp/2017/ja/sponsors/'
       res = requests.get(url)
       content = res.content

* 次にHTMLをBeautiful Soup 4に渡して解析します。HTMLの解析についてはもう少し詳しく説明します。

.. code-block:: python
   :caption: WebページをBeautiful Soup 4で解析

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
Beautiful Soup 4でHTMLを解析して、値が取り出せましたが、どのように指定しているのでしょうか?
スポンサー一覧のHTMLを見てみると、以下のような形式になっています。(:numref:`sponsor-list-html`)

.. _sponsor-list-html:

.. code-block:: html
   :caption: スポンサー一覧のHTML
   :emphasize-lines: 6,8,12

   <div class="span12">
     <h2>Diamond</h2>
     <div class="row">
       <div class="span4">
         <div class="sponsor" id="sponsor-5">
           <div class="sponsor-content">
             <h3>
               <a href="https://squeeze-inc.co.jp/">
                 <img src="/2017/site_media/media/sponsor_files/squeeze-logo-horizontal_1.png.150x80_q85.png" alt="株式会社SQUEEZE" />
               </a>
             </h3>
             <h4>株式会社SQUEEZE</h4>
             <p><a href="https://squeeze-inc.co.jp/">https://squeeze-inc.co.jp/</a></p>
             <p>
               <p>株式会社SQUEEZEでは「価値の詰まった社会を創る」ことをミッションとしております。ICTの力で地域コミュニティが持つ資産の潜在的な「価値」を活かし、社会に提供していくことで「無駄」のない「価値の詰まった」社会を創造していきます。</p>
               <p>主要事業として、ホテル・旅館・民泊に特化したサービスを提供・運営しています。ホスピタリティテックのリーディングカンパニーとして、人材の再発掘・活用による働き方改革、空き家問題解消による地域活性化、を牽引するナンバーワンのプラットフォームになることを目指しています。</p>
             </p>
           </div>
         </div>
       </div>
     </div>
   </div>
   <div class="span12">
     <h2>Platinum</h2>
       <div class="row">
         <div class="span4">
           <div class="sponsor" id="sponsor-7">
             <div class="sponsor-content">
               <h3>
                 <a href="https://recruit.monotaro.com/?utm_medium=outside_flier&amp;utm_source=pycon.jp&amp;utm_campaign=PyConJP2017">
                   <img src="/2017/site_media/media/sponsor_files/logo-PyCon2017.png.150x80_q85.png" alt="株式会社MonotaRO" />
                 </a>
               </h3>
               <h4>株式会社MonotaRO</h4>
               <p><a href="https://recruit.monotaro.com/?utm_medium=outside_flier&amp;utm_source=pycon.jp&amp;utm_campaign=PyConJP2017">https://recruit.monotaro.com/?utm_medium=outside_flier&amp;utm_source=pycon.jp&amp;utm_campaign=PyConJP2017</a></p>
               <p>
                 <p>「ITで、間接資材調達を変革する」<br />モノタロウは働く現場で必要となる様々な間接資材(最終製品となる原材料を除く全ての資材)約1,000万点をインターネットで販売しています。<br />様々な現場のニーズにお応えすべく、自社開発の高度な検索システムと精緻なデータベースマーケティングが実現する「お客様ごとの最適化したレコメンドサービス」で従来の非効率的な間接資材調達を変革し社会に新しい価値を提供しています。</p>
               </p>
             </div>
   (以下続く)

このHTMLを見ると、スポンサーの名前とURLは以下のようにして取得できそうです。

* 一つのスポンサーの情報は ``<div class="sponsor-content">`` の中に入っている
* スポンサーのURLは ``<h3>`` タグの中の ``<a>`` タグの ``href`` アトリビュートに入っている
* スポンサー名は ``<h4>`` タグで囲まれた中に入っている

HTMLの構造がわかったところで、もう一度HTMLを解析しているコードを見てみます。

.. index:: html.parser

.. code-block:: python
   :caption: WebページをBeautiful Soup 4で解析

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
RequestsやBeautiful Soup 4の動作を変えて、さまざまなWebページから色んな要素を取得できます。

以下にそれぞれのライブラリの簡単な使い方を紹介します。それ以外にもいろいろな使用方法があるので、ドキュメントを参考にしていろいろ作り変えてみてください。

.. index:: Requests

Requests の主な使い方
---------------------
ここでは Requests の主な使い方の例をいくつか載せます。
詳細については以下の公式ドキュメントを参照してください。

:公式ドキュメント: `Requests: HTTP for Humans <https://requests.readthedocs.io/>`_

以下は認証つきのURLにアクセスして、結果を取得する例です。

.. code-block:: pycon
   :caption: 認証付きURLにアクセスする

   >>> import requests
   >>> r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
   >>> r.status_code
   200

.. index:: Requests
    single: Requests; POST

POST を行う場合は以下のように、POSTのパラメーターを辞書で定義します。

.. code-block:: pycon
   :caption: requests で POST する

   >>> payload = {'key1': 'value1', 'key2': 'value2'} # POST するパラメーター
   >>> r = requests.post('http://httpbin.org/post', data=payload)
   >>> print(r.text)

.. index:: Requests
    single: Requests; GET

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

Beautiful Soup 4の主な使い方
----------------------------
ここではBeautiful Soup 4の主な使い方の例をいくつか載せます。
詳細については以下の公式ドキュメントを参照してください。

.. index:: Beautiful Soup 4
    single: Beautiful Soup 4; Documentation

:公式ドキュメント: `Beautiful Soup Documentation <https://www.crummy.com/software/BeautifulSoup/bs4/doc/>`_

.. code-block:: pycon
   :caption: Beautiful Soup 4の使用例

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

.. index:: find/find_all
    single: Beautiful Soup 4; find()
    single: Beautiful Soup 4; find_all()

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
======
本節では、Pythonでスクレイピングをする方法を解説しました。

RequestsとBeautiful Soup 4を使いこなすことにより、さまざまなウェブサイトから情報を取得できるようになります。

なお、短時間にWebサイトに大量にアクセスをすると迷惑となるので、そういうことがないようにプログラムを実行するときには注意してください。

参考書籍
========
Pythonでのスクレイピングについてもいくつか書籍が出ています。

- `PythonによるWebスクレイピング <https://www.oreilly.co.jp/books/9784873117614/>`_
- `Pythonクローリング＆スクレイピング ―データ収集・解析のための実践開発ガイド <http://gihyo.jp/book/2017/978-4-7741-8367-1>`_
- `Pythonによるスクレイピング＆機械学習 開発テクニックBeautifulSoup、scikit-learn、TensorFlowを使ってみよう <http://www.socym.co.jp/book/1079>`_
- `Pythonエンジニア ファーストブック <http://gihyo.jp/book/2017/978-4-7741-9222-2>`_ (第4章 PythonによるWebスクレイピング)
