```{index} venv
```

(venv-section)=

# サードパーティ製パッケージと venv

```{admonition} 節サブタイトル
隔離されたPythonの実行環境で便利なサードパーティ製パッケージを利用する。
```

本節では、Pythonをより便利にするサードパーティ製パッケージのインストール方法と、環境を壊さずにインストールするための venv モジュールの使い方を説明します。

```{index} PyPI
```

## サードパーティ製パッケージ

Python は標準ライブラリだけでもいろいろなことができますが、さらに便利なサードパーティ製のパッケージも提供されています。

サードパーティ製パッケージは [PyPI](https://pypi.org/) （the Python Package Index、パイピーアイと読む）というサイトで情報が共有されています。

```{figure} images/pypi.png
:alt: PyPI - the Python Package Index
:width: 600

PyPI - the Python Package Index
```

```{index} pip
```

### pipコマンド

サードパーティ製パッケージをインストールするには、 **pipコマンド** を使用します。

**以下はpipコマンドのサンプルです** ここでは実行しないで、以下のvenv環境を作ってから実行しましょう。
pip コマンドを利用すると以下の様なコマンドで簡単にサードパーティ製パッケージをインストールできます。

```{index} requests single: pip; requests
```

```{code-block} sh
:caption: "pipコマンドで (パッケージ名) をインストール"

$ pip install パッケージ名
```

次に、独立したPython環境を構築する **venv** モジュールについて説明します。

```{admonition} コラム: Windows環境でpip実行時にエラーになる場合
PATH環境変数を確認し、Python 3 をインストールしているPATHが設定されているかどうか確認してみてください。
```

<!--
# pip自体のアップグレードが必要なケースが以前より減っているため、
# 入門テキストで紹介しなくても良いと思います。
-->

````{admonition} コラム: pip自身のアップグレード
pip自身もpipコマンドでアップグレードを行えます。
アップグレードは、次のコマンドを実行します。

```{code-block} sh
:caption: "pipをアップグレード(macOS、Linux)"

$ pip install pip --upgrade
```

Windowsの場合、このコマンドを実行すると現在入っているpipが削除されたうえに最新バージョンのpipのインストールに失敗してpipが使えなくなることがたまに発生します。以下のコマンドを使ってください。

```{code-block} sh
:caption: "pipをアップグレード(Windows)"

 > python -m pip install --upgrade pip
```
````

```{index} venv single: venv; Virtual Environments
```

(about-venv)=

## venvとは

複数のプロジェクトで異なるサードパーティ製パッケージを利用することはよくあります。その場合、プロジェクトごとにインストールするパッケージを切り替えられると便利です。

venvはプロジェクトごとに隔離されたPythonの仮想環境(Virtual Environments)を作成します。

```{figure} images/venv-image.png
:alt: venvのイメージ
:width: 600

venvのイメージ
```

:::{admonition} コラム: condaの場合
[Anaconda](https://www.anaconda.com/products/distribution) を使っている場合は **pip** 、 **venv** の代わりに [Conda](https://docs.conda.io/en/latest/) というパッケージ管理ツールを使用します。

condaではそれぞれ以下のコマンドで、サードパーティ製パッケージのインストール、環境の作成、有効化、無効化が行えます。

```{code-block} sh
:caption: "conda コマンドの例"

$ conda create --name env python  # 環境を作成
$ source activate env  # 環境の有効化
(env) $ conda install requests  # パッケージのインストール
(env) $ source deactivate  # 環境の無効化
```
:::

### venv環境の作成

venv環境を作成します。

作成には `venv` モジュールを使用します。引数には作成する環境の名前を指定します。

(venv-create-linux-or-mac)=

```{code-block} sh
:caption: "venv環境の作成(macOS、Linux)"

 $ python3 -m venv env
 $ ls
 env/
```

Windowsの場合はスクリプトの実行権限を与えます（`Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` ）。このコマンドは一度実行したら、再び実行する必要はありません。

```{code-block} sh
:caption: "venv環境の作成(Windows)"

 > Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
 > python -m venv env
 > ls
 env/
```

現在のフォルダに、envというディレクトリが作成されます。

### venv環境の有効化

作成した `venv` 環境を有効化（activate）します。

```{index} source
```

```{index} activate
```

そのためにはbashスクリプトの `env/bin/activate` を `source` コマンドで実行します（{numref}`venv-activate-linux-or-mac` ）。
Windowsの場合はスクリプトを実行します（ {numref}`venv-activate-windows` ）。

(venv-activate-linux-or-mac)=

```{code-block} sh
:caption: "venv環境の有効化(macOS、Linux)"

 $ source env/bin/activate
 (env) $
```

(venv-activate-windows)=

```{code-block} sh
:caption: "venv環境の有効化(Windows)"

 > env\Scripts\Activate.ps1
 (env) >
```

`venv` 環境を有効化すると、プロンプトの前に環境名（ここでは `env` ）が表示されます。そして、環境変数 `PATH` の先頭にenv/binが追加され、 `venv` 環境のPythonが実行されるようになります。

ここでは、 `pip` コマンドで `requests` （HTTPクライアントのパッケージ）をインストールします（{numref}`venv-install-requests`）。

(venv-install-requests)=

```{code-block} sh
:caption: "パッケージのインストール"

 (env) $ pip install requests
 (env) $ python
 >>> import requests
 >>> # requestsがインポートできる
```

`requests` が `env/lib/python3.12/site-packages` 配下にインストールされます。

またPythonパッケージの中にはコマンドとして実行可能なファイルが含まれている場合があります。それらのファイルは `env/bin` 配下にインストールされます。

```{index} deactivate
```

### venv環境の無効化

`venv` 環境を無効化（deactivate）するには、 `deactivate` コマンドを実行します（{numref}`venv-deactivate`）。

無効化した後、元の環境で `requests` をインポートするとエラーとなり、 `venv` 環境でのみ `requests` がインストールされていることがわかります。

(venv-deactivate)=

```{code-block} sh
:caption: "venv環境を無効化"

 (env) $ deactivate
 $
 $ python
 >>> import requests
 Traceback (most recent call last):
   File "<stdin>", line 1, in <module>
 ModuleNotFoundError: No module named 'requests'
 >>> # エラーが出力される
```

```{index} freeze single: pip; freeze single: pip; requirements.txt
```

:::{admonition} コラム: 仮想環境の共有(pip freezeとrequirements.txt)
venvで仮想環境を作成できることの必要性はわかってもらえたと思います。
あるプロジェクトを複数人で開発する場合に、インストールしているパッケージ情報はどのように共有するのでしょうか?

pipにはそのための機能があります。
`pip freeze` コマンドを実行すると、インストールしたパッケージの一覧が出力されます。
この情報をファイルに保存して、プログラムのソースコードと一緒にバージョン管理します。
ファイル名としては **requirements.txt** がよく知られている名前なので、他の人にパッケージの一覧が入っているという意図が伝わりやすいです。

```{code-block} sh
:caption: pip freeze コマンドでパッケージの情報を書き出す

(env) $ pip install requests
(env) $ pip freeze > requirements.txt
(env) $ cat requirements.txt
certifi==2017.4.17
chardet==3.0.4
idna==2.5
requests==2.18.1
urllib3==1.21.1
```

プロジェクトの他のメンバーは、ソースコードをダウンロードした後、以下の手順で仮想環境に同じパッケージをインストールします。

```{code-block} sh
:caption:  pip install で同じ環境を作る

$ git clone https://github.com/pyconjp/some-project.git
$ cd some-project
$ python3 -m venv env  # Windowsの場合は python -m venv env
$ source env/bin/activate
(env) $ pip install -r requirements.txt
Collecting certifi==2017.4.17 (from -r hoge.txt (line 1))
  Using cached certifi-2017.4.17-py2.py3-none-any.whl
(中略)
Installing collected packages: certifi, chardet, idna, urllib3, requests
Successfully installed certifi-2017.4.17 chardet-3.0.4 idna-2.5 requests-2.18.1 urllib3-1.21.1
(env) $
```

このようにして、同一の環境をプロジェクトメンバー全体で共有します。
:::

```{index} conda
```

## まとめ

本節では、以下について説明しました。

- 便利なサードパーティ製パッケージのサイト **PyPI**
- パッケージをインストールする **pipコマンド**
- プロジェクトごとに隔離したPython環境を、 **venvモジュール** を使って作成、有効化、無効化する方法

次節では、venv環境にパッケージをインストールして、スクレイピングを行う方法を説明します。
