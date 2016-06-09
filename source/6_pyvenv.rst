.. -*- coding: utf-8 -*-

.. _pyvenv-section:

=====================================
 サードパーティ製パッケージと pyvenv
=====================================

:節サブタイトル: 隔離されたPythonの実行環境で便利なサードパーティ製パッケージを利用する。

本節では、Pythonをより便利にするサードパーティ製パッケージのインストール方法と、環境を壊さずにインストールするための pyvenv コマンドの使い方を説明します。

サードパーティ製パッケージ
==========================
Python は標準ライブラリだけでもいろいろなことができますが、さらに便利なサードパーティ製のパッケージも提供されています。

サードパーティ製パッケージは `PyPI <https://pypi.python.org>`_ (the Python Package Index、パイピーアイと読む)というサイトで情報が共有されています。

.. figure:: images/pypi.png
   :width: 600
   :alt: PyPI - the Python Package Index

   PyPI - the Python Package Index

pipコマンド
-----------
サードパーティ製パッケージをインストールするには、 **pipコマンド** を使用します。

Python 3.5.1では ``ensurepip`` という仕組みによって、Pythonのインストール時にpipコマンドがインストールされます。

現在イントールされているpipコマンドを最新にアップグレードするには、次のコマンドを実行します。

.. code-block:: sh
   :caption: pipをアップグレード

   $ sudo pip install pip --upgrade

pip コマンドを利用すると以下の様なコマンドで簡単にサードパーティ製パッケージをインストールできます。

.. code-block:: sh
   :caption: pipコマンドでrequestsをインストール

   $ pip install requests

しかし、その前に独立したPython環境を構築する **pyenv** について説明します。

pyvenvとは
==========

複数のプロジェクトで異なるサードパーティ製パッケージを利用することはよくあります。その場合、プロジェクトごとにインストールするパッケージを切り替えられると便利です。

pyvenvはプロジェクトごとに隔離されたPython環境を作成します。

pyvenv環境の作成
----------------

pyvenv環境を作成します。

作成には ``pyvenv`` コマンドを使用します。引数には作成する環境の名前を指定します。

.. code-block:: sh
   :caption: pyvenv環境の作成

    $ pyvenv env

カレントディレクトリに、envというディレクトリが作成されます。

pyvenv環境の有効化
------------------

作成した ``pyvenv`` 環境を有効化（activate）します。

そのためにはbashスクリプトの ``env/bin/activate`` を ``source`` コマンドで実行します（:numref:`pyvenv-activate`）。

.. _pyvenv-activate:

.. code-block:: sh
   :caption:  pyvenv環境の有効化

    $ source env/bin/activate
    (env)$

``pyvenv`` 環境を有効化すると、プロンプトの前に環境名（ここでは ``env`` ）が表示されます。そして、環境変数 ``PATH`` の先頭にenv/binが追加され、 ``pyvenv`` 環境のPythonが実行されるようになります。

ここでは、 ``pip`` コマンドで ``requests`` （HTTPクライアントのパッケージ）をインストールします（:numref:`pyvenv-install-requests`）。

.. _pyvenv-install-requests:

.. code-block:: sh
   :caption: パッケージのインストール

    (env)$ pip install requests
    (env)$ python
    >>> import requests
    >>> # requestsがインポートできる

``requests`` が ``env/lib/python3.5/site-packages`` 配下にインストールされます。

またPythonパッケージの中にはコマンドとして実行可能なファイルが含まれている場合があります。それらのファイルは ``env/bin`` 配下にインストールされます。

pyvenv環境の無効化
------------------
``pyvenv`` 環境を無効化（deactivate）するには、 ``deactivate`` コマンドを実行します（:numref:`pyvenv-deactivate`）。

無効化した後、元の環境で ``requests`` をインポートするとエラーとなり、 ``pyvenv`` 環境でのみ ``requests`` がインストールされていることがわかります。

.. _pyvenv-deactivate:

.. code-block:: sh
   :caption: pyvenv環境を無効化

    (env)$ deactivate
    $
    $ python
    >>> import requests
    Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
    ImportError: No module named requests
    >>> # エラーが出力される


まとめ
=======

本節では、以下について説明しました。

- 便利なサードパーティ製パッケージのサイト **PyPI**
- パッケージをインストールする **pipコマンド**
- プロジェクトごとに隔離したPython環境を、 **pyvenvコマンド** を使って作成、有効化、無効化する方法

次節では、pyvenv環境にパッケージをインストールして、スクレイピングを行う方法を説明します。
