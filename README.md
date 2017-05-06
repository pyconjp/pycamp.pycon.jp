# pycamp.pycon.jp

[![Documentation Status](https://readthedocs.org/projects/bootcamp-text/badge/?version=latest)](http://bootcamp-text.readthedocs.io/?badge=latest)

* ビルドされたページ: http://pycamp.pycon.jp/
* Read the Docs のプロジェクトページ: Read https://readthedocs.org/projects/bootcamp-text/
* www.pycon.jp の説明ページ: https://www.pycon.jp/support/bootcamp.html

## How to build

```
$ git clone git@github.com:pyconjp/pycamp.pycon.jp.git
$ cd pycamp.pycon.jp
$ python3.6 -m venv env
$ . env/bin/activate
(env) $ pip install -r requirements.txt
(env) $ make html
(env) $ open build/html/index.html
```
