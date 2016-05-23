.. -*- coding: utf-8 -*-

.. _pyvenv-section:

============
 pyvenv
============

:節サブタイトル: 隔離されたPythonの実行環境

本節では、pyvenvを用いた隔離されたPythonの実行環境の作り方と使い方を説明します。

はじめに
========

複数のプロジェクトで異なるサードパーティ製パッケージを利用することはよくあります。その場合、プロジェクトごとにインストールするパッケージを切り替えられると便利です。

pyvenvはプロジェクトごとに隔離された環境を作成します。


pyvenv環境の作成
====================

pyvenv環境を作成します。

作成には ``pyvenv`` コマンドを使用します。引数には作成する環境の名前を指定します。

.. code-block:: sh
   :caption: pyvenv環境の作成

    $ pyvenv env

カレントディレクトリに、envというディレクトリが作成されます。

pyvenv環境の有効化
======================

作成した ``pyvenv`` 環境を有効化（activate）します。

そのためにはbashスクリプトのenv/bin/activateを ``source`` コマンドで実行します（:numref:`pyvenv-activate`）。

.. _pyvenv-activate:

.. code-block:: sh
   :caption:  pyvenv環境の有効化

    $ source env/bin/activate
    (env)$

``pyvenv`` 環境を有効化すると、プロンプトの前に環境名（ここでは ``env`` ）が表示されます。そして、環境変数 ``PATH`` の先頭にenv/binが追加され、 ``pyvenv`` 環境のPythonが実行されるようになります。

例として、 ``pip`` というPython公式のパッケージリポジトリからパッケージをインストールできるコマンドで ``requests`` （HTTPクライアントのパッケージ）をインストールします（:numref:`pyvenv-install-requests`）。

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
======================

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

本節では、プロジェクトごとに隔離した ``pyvenv`` 環境について、作成、有効化／無効化を行う方法を説明しました。

次節では、それを使ってスクレイピングを行う方法を記述します。
