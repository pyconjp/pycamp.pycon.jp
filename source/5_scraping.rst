==================================
スクレイピング
==================================

:節サブタイトル: 自動でデータを収集する方法

そもそもスクレイピングとは
=====================
ウェブサイトから情報を抽出する、コンピュータソフトウェア技術のことをいいます。

Pythonを使って実行することができますので、これを機に習得してみましょう。


環境構築
=====================
下記コマンドを実行を実行すれば、完了です。

* pip install requests
* pip install beautifulsoup4


目的
=====================
#. スクレイピングでpypiの新着パッケージ情報を取得してみましょう
#. 取得した情報をjsonで保存して見ましょう


用語説明
=====================
* pip：Pythonで書かれたパッケージソフトウェアをインストール・管理するためのパッケージ管理システムです。
* pypi：Python公式のパッケージリポジトリです。pipコマンドを実行して、リポジトリに配置されているパッケージを取得することができます。
* json：データを記述する書式です。


実際のコード
=====================

下記コードをsimple.pyという名前で保存して見ましょう

.. code-block:: python

    #! /usr/bin/env python
    # -*- coding: utf-8 -*-
    import sys
    import json
    import argparse
    import requests
    from bs4 import BeautifulSoup


    def main(argv=sys.argv[1:]):
        parser = argparse.ArgumentParser()
        parser.add_argument('-o', '--output', default=sys.stdout, type=argparse.FileType('w'))
        args = parser.parse_args(argv)

        url = 'https://pypi.python.org/pypi'
        res = requests.get(url)
        soup = BeautifulSoup(res.content, 'html.parser')
        records = soup.select('div.section table.list tr')
        iter_records = iter(records)
        next(iter_records)  # table header

        data = []
        for record in iter_records:
            tds = record.findAll('td')
            if tds[0].get('id') == 'last':
                break
            atag = tds[1].find('a')
            data.append({
                'title': atag.text,
                'url': atag.get('href'),
                'description': tds[2].text,
            })

        json.dump(data, args.output)

    if __name__ == '__main__':
        sys.exit(main())


コードの説明
=====================
* 「#! /usr/bin/env python」って何？
    Pythonを簡単に実行するためのおまじないのようなものです。
    詳しくはShebang(シェバン)といいます。

* 「# -*- coding: utf-8 -*-」って何？
    このソースががUTF-8で書かれていることを示します。
    エディター(Emacs)等で開く際に参照されます。

* 「sys.exit」って何？
    明示的にプログラムを終了させるコードになります。

* 「[1:]」って何？
    配列から値を取得する際の記述方法のうちのひとつです。
    この場合だと、配列の2番目以降の情報をすべて取得することができます。

* 「BeautifulSoup」って何？
　　HTMLを解析するライブラリになります。

.. code-block:: python

    from bs4 import BeautifulSoup
    soup = BeautifulSoup('<div><h1 id="test">TEST</h1></div>', 'html')
    soup.select_one('div h1#test').text
.. code-block:: python
    とすると、「'TEST'」と表示されます。

* 「json.dump」って何？
    指定されたオブジェクトをJSON文字列に変換することができます。

    この場合、オブジェクト(data)を指定したファイル(--outputオプション)に保存します。


実行してみよう
==========
simple.py --output output.json


実行したら、output.jsonが作成されていますので、中身を参照してみてください。

pypiの情報がまとめて保存されていることがわかります。


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

- pypi情報取得サンプル https://github.com/TakesxiSximada/happy-scraping/tree/master/pypi.python.org

- Pythonスクレイピングメモ http://qiita.com/TakesxiSximada/items/0944d989e72fa8ac8f3a
