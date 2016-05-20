==================================
スクレイピング
==================================


.. _guide-module:

そもそもスクレイピングとは
=====================
ウェブサイトから情報を抽出するコンピュータソフトウェア技術のこと。
WWWから自動的に情報を収集する処理。

wiki(https://ja.wikipedia.org/wiki/%E3%82%A6%E3%82%A7%E3%83%96%E3%82%B9%E3%82%AF%E3%83%AC%E3%82%A4%E3%83%94%E3%83%B3%E3%82%B0)より抜粋


環境構築
=====================

下記コマンドを実行

pip install requests

pip install beautifulsoup4



ではやってみよう
=====================
目的：

#. スクレイピングでpypiの新着パッケージ情報を取得する
#. 取得した情報をjsonで保存する


用語説明
=====================
* pypiとは：(pypiの説明)
* jsonとは：(jsonの説明)


実際のコード
=====================

下記コードをsimple.pyという名前で保存

| #! /usr/bin/env python
| # -*- coding: utf-8 -*-
| import sys
| import json
| import argparse
| import requests
| from bs4 import BeautifulSoup
|
|
| def main(argv=sys.argv[1:]):
|     parser = argparse.ArgumentParser()
|     parser.add_argument('-o', '--output', default=sys.stdout, type=argparse.FileType('w'))
|     args = parser.parse_args(argv)
|
|     url = 'https://pypi.python.org/pypi'
|     res = requests.get(url)
|     soup = BeautifulSoup(res.content, 'html.parser')
|     records = soup.select('div.section table.list tr')
|     iter_records = iter(records)
|     next(iter_records)  # table header
|
|     data = []
|     for record in iter_records:
|         tds = record.findAll('td')
|         if tds[0].get('id') == 'last':
|             break
|         atag = tds[1].find('a')
|         data.append({
|             'title': atag.text,
|             'url': atag.get('href'),
|             'description': tds[2].text,
|         })
|
|     json.dump(data, args.output)
|
| if __name__ == '__main__':
|     sys.exit(main())


コードの説明
=====================
* 「#! /usr/bin/env python」って何？
* 「# -*- coding: utf-8 -*-」って何？
* 「sys.exit」って何？
* 「[1:]」って何？
* 「BeautifulSoup」って何？
* 「json.dump」って何？


実行してみよう
==========
python simple.py --output output.json


まとめ
==========
本節では、Pythonでスクレイピングをする方法を解説しました。
自動化することにより、作業を効率化することができます。
目的に応じて処理を記述していきましょう。


参考
==========
- requests http://requests-docs-ja.readthedocs.io/en/latest/

- pypi情報取得サンプル https://github.com/TakesxiSximada/happy-scraping/tree/master/pypi.python.org

- Pythonスクレイピングメモ http://qiita.com/TakesxiSximada/items/0944d989e72fa8ac8f3a
