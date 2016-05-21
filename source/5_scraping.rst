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
その後、pipコマンドを実行し、下記ライブラリを利用可能な状態にしてください。

* pip install requests
* pip install beautifulsoup4


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
=====================
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


実行してみよう
==============
作成した環境にactivateした後、下記のコマンドを実行してみましょう

python simple.py

実行すると、Pythonに関する新着ニュースが表示されることが確認できます。


まとめ
==========
本節では、Pythonでスクレイピングをする方法を解説しました。

自動化することにより、作業を効率化することができます。

目的に応じて処理を記述していきましょう。


参考
==========
- wikipedia(スクレイピング) https://ja.wikipedia.org/wiki/ウェブスクレイピング

- wikipedia(pip) https://ja.wikipedia.org/wiki/Pip

- requests http://requests-docs-ja.readthedocs.io/en/latest/

