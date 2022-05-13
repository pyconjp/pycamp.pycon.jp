.. _guide-install:

======================
 Pythonをはじめる前に
======================

:節サブタイトル: エディタ、コマンドラインの準備、Pythonのインストール方法の紹介

Pythonをはじめましょう！

本節では Python Boot Camp の事前準備として以下について説明します。

- ソースコードを読み書きするためのエディタの準備
- Python を実行するためのコマンドラインの準備
- Pythonのインストール方法

.. index:: Editor
    single: Editor; Atom

エディタの準備
==============
ソースコードを読み書きするために、エディタを用意します。
普段使用しているエディタがある人は、そのエディタを使用して構いません。
Python の文法に対応しているエディタを使用することをおすすめします。

普段使っているエディタがない人は、 `Atom <https://atom.io/>`_ をインストールしてください。
Atomはさまざまなプログラミング言語に対応したエディタで、拡張機能も豊富です。

.. index:: Terminal

ターミナルの準備
================
Python を実行するために、ターミナル(macOS)、PowerShell(Windows)を立ち上げます。

- macOS では「アプリケーション」→「ユーティリティ」→「ターミナル」を選択します
- Windows では **Windows+R** キーを押して ``powershell`` と入力します

.. index:: Install

.. _python-install:

Pythonのインストール
====================

ここではPythonのインストール方法を説明します。

macOS、Windows、Linuxの3つの環境でのインストール手順を説明します。

.. index::
    single: Install; macOS

macOSの場合
-----------
macOSでPythonを利用する場合は、Pythonの公式サイトで配布されているビルド済みのパッケージをインストールします。

「 `Python Release Python 3.10.4 <https://www.python.org/downloads/release/python-3104/>`_ 」をブラウザで開きます。
以下をダウンロードして実行し、Pythonをインストールします。

- `macOS 64-bit universal2 installer <https://www.python.org/ftp/python/3.10.4/python-3.10.4-macos11.pkg>`_

詳しくはPythonの公式ドキュメントの「 `MacintoshでPythonを使う <https://docs.python.org/ja/3/using/mac.html>`_ 」を参考にしてください。

インストールが完了したらPythonのバージョンが3.10.4になっていることを確認します（:numref:`check-version-mac`）。

.. _check-version-mac:

.. code-block:: bash
   :caption: Pythonのバージョンを確認

   $ python3 -V
   Python 3.10.4

.. index::
    single: Install; Windows

Windowsの場合
-------------

WindowsでPythonを利用する場合は、Pythonの公式サイトで配布されているWindowsインストーラを利用します。

「 `Python Release Python 3.10.4 <https://www.python.org/downloads/release/python-3104/>`_ 」をブラウザで開きます。
OSによって以下のいずれかのインストーラーをダウンロードし、ウィザードに従ってインストールします。

- 64ビット版: `Windows installer (64-bit) <https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe>`_
- 32ビット版: `Windows installer (32-bit) <https://www.python.org/ftp/python/3.10.4/python-3.10.4.exe>`_

この時、「Add Python 3.10 to PATH」にチェックを入れておきましょう。自動的に必要な環境変数が設定されます（:numref:`windows-install`）。

.. _windows-install:

.. figure:: images/pythonforwindows1.png
   :width: 600

   Python for Windowsのインストール画面

.. index::
    single: Install; Linux

インストールが完了したらPythonのバージョンが3.10.4になっていることを確認します（:numref:`check-version-win`）。

.. _check-version-win:

.. code-block:: doscon
   :caption: Pythonのバージョンを確認

   C:\Users\user>python -V
   Python 3.10.4

Linux（Ubuntu Server）の場合
----------------------------
Ubuntu 22.04にはデフォルトでPython 3.10.4がインストールされています。
以下のコマンドでPythonのバージョンを確認します（:numref:`check-version`）。

.. _check-version:

.. code-block:: bash
   :caption: Pythonのバージョンを確認

   $ python3 -V
   Python 3.10.4

注意事項
========
これ以降の本テキストでは上記手順でインストールしたPython 3.8以降を使用することを前提に記載しています。

Python 2.7等のPython2系やAnacondaでインストールしたPythonでは実習ができません。

Pythonを起動した時に表示される文字をチェックして、下記が問題ないか確認してください。

- Pythonのバージョン(3.8以上であること)
- Anacondaという文字が表示されないこと

インストールされていない場合は前述の手順でPython3.10.4のインストールを行ってください。

まとめ
======
本節では、事前準備としてエディタ、コマンドラインとPython のインストール方法を紹介しました。
次節ではFizzBuzzを通じたPythonの特徴、基本、役立つWeb の情報、書籍を紹介します。
