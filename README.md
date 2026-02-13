# pycamp.pycon.jp

[![Documentation Status](https://readthedocs.org/projects/bootcamp-text/badge/?version=latest)](http://bootcamp-text.readthedocs.io/?badge=latest)

* ビルドされたページ: http://pycamp.pycon.jp/
* Read the Docs のプロジェクトページ: Read https://readthedocs.org/projects/bootcamp-text/
* www.pycon.jp の説明ページ: https://www.pycon.jp/support/bootcamp.html

## ビルド環境準備

Ubuntu環境でのフォントインストール
```
$ sudo apt update
$ sudo apt install fonts-noto-cjk
$ rm -rf ~/.cache/matplotlib
```

### コンテナ環境を利用したビルド環境準備
- この手順は必須ではありません
- コンテナ環境を利用して、貢献者同士の開発環境を統一することができる
設定ファイルは [.devcontainer/devcontainer.json](.devcontainer/devcontainer.json)

- Visual Studio Codeの拡張機能を利用する場合 (ローカル環境)
[Visual Studio Code を使用して Docker コンテナーを開発環境として使用する - Training | Microsoft Learn](https://learn.microsoft.com/ja-jp/training/modules/use-docker-container-dev-env-vs-code/)

- GitHub Codespacesを使用する場合 (リモート環境)
[GitHub Codespacesのクイックスタート](https://docs.github.com/ja/codespaces/getting-started/quickstart)

## How to build(macOSまたはLinux)

```
$ git clone git@github.com:pyconjp/pycamp.pycon.jp.git
$ cd pycamp.pycon.jp
$ python3.13 -m venv env
$ . env/bin/activate
(env) $ pip install -r requirements.txt
(env) $ make html
(env) $ python -m http.server -d build/html # http://127.0.0.1:8000/ をブラウザで開くとHTMLの内容を確認できる
```

## How to build(windows powershell)

```
$ git clone git@github.com:pyconjp/pycamp.pycon.jp.git
$ cd pycamp.pycon.jp
$ py -3.13 -m venv env
$ .\env\Scripts\Activate.ps1
(env) $ pip install -r requirements.txt
(env) $ make html
(env) $ python -m http.server -d build/html # http://127.0.0.1:8000/ をブラウザで開くとHTMLの内容を確認できる
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


# 注意: 最新の Sphinx は Python 3.11 以上が必要。3.10 以下では環境構築が不可。
以下のエラーが発生する。
ERROR: Could not find a version that satisfies the requirement Sphinx==8.2.3 (from versions: 0.1.61611, 0.1.61798, 0.1.61843, ・・・・・省略
ERROR: No matching distribution found for Sphinx==8.2.3


# Markdownlint について

Markdown ファイルを Lint するために、Pull Requests の発行時に Markdownlint が実行されるようになっています。

サプライチェーン攻撃を防ぐために、バージョンはコミットハッシュで固定されています。
