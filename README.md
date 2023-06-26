# pycamp.pycon.jp

[![Documentation Status](https://readthedocs.org/projects/bootcamp-text/badge/?version=latest)](http://bootcamp-text.readthedocs.io/?badge=latest)

* ビルドされたページ: http://pycamp.pycon.jp/
* Read the Docs のプロジェクトページ: Read https://readthedocs.org/projects/bootcamp-text/
* www.pycon.jp の説明ページ: https://www.pycon.jp/support/bootcamp.html

## How to build

```
$ git clone git@github.com:pyconjp/pycamp.pycon.jp.git
$ cd pycamp.pycon.jp
$ python3.11 -m venv env
$ . env/bin/activate
(env) $ pip install -r requirements.txt
(env) $ make html
(env) $ open build/html/index.html
```

## テキスト修正の提案方法

1. pycamp.pycon.jpリポジトリをforkする
2. forkしたリポジトリをcloneする
3. cloneしたリポジトリのmasterに、修正したテキスト内容をpushする
4. PRを作成する

## reStructuredTextとmarkdownについて

* Python Boot Campテキスト(`source/textbook/` 以下)と貢献者一覧ページ(`source/organize/3_contributers.md`)はmarkdownで記述しています
  * markdownはSphinxの拡張表現(directive)に対応した**MyST**を使っています
  * MySTの記述ルールについては[myst-parser](https://myst-parser.readthedocs.io/)を参照してください
  * とはいえ、directiveを使わないのであれば通常のmarkdownと同じです
* それ以外のページはreStructuredTextで記述しています
