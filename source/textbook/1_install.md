(guide-install)=

# Pythonをはじめる前に

```{admonition} 節サブタイトル
エディタ、コマンドラインの準備、Pythonのインストール方法の紹介
```

Pythonをはじめましょう！

本節では Python Boot Camp の事前準備として以下について説明します。

- ソースコードを読み書きするためのエディタの準備
- Python を実行するためのコマンドラインの準備
- Pythonのインストール方法

```{index} Editor single: Editor; VS Code
```

## エディタの準備

ソースコードを読み書きするために、エディタを用意します。
普段使用しているエディタがある人は、そのエディタを使用して構いません。
Python の文法に対応しているエディタを使用することをおすすめします。

普段使っているエディタがない人は、 [Visual Studio Code](https://code.visualstudio.com/) をインストールしてください。
Visual Studio Codeはさまざまなプログラミング言語に対応したエディタで、拡張機能も豊富です。

Visual Studio CodeとPython用拡張機能のインストール手順は以下のページを参考にしてください。

- [IDE(エディタ) — Pythonスターターガイド ドキュメント](https://starter-guide.od.pythonic-exam.com/ja/latest/ide/index.html)
- [Visual Studio Codeのインストール: Visual Studio Code でPython入門 【Windows編】 - python.jp](https://www.python.jp/python_vscode/windows/setup/install_vscode.html)

```{index} Terminal
```

## ターミナルの準備

Python を実行するために、ターミナル(macOS)、PowerShell(Windows)または、Visual Studio Code 内のターミナルを立ち上げます。

- macOS では「アプリケーション」→「ユーティリティ」→「ターミナル」を選択します
- Windows では **Windows+R** キーを押して `powershell` と入力します（このテキストではコマンドプロンプトは使いません）
- Visual Studio Codeではメニューから「表示」→「ターミナル」を選択します

```{index} Install
```

(python-install)=

## Pythonのインストール

ここではPythonのインストール方法を説明します。

macOS、Windows、Linuxの3つの環境でのインストール手順を説明します。

```{index} single: Install; macOS
```

### macOSの場合

macOSでPythonを利用する場合は、Pythonの公式サイトで配布されているビルド済みのパッケージをインストールします。

「 [Python Release Python 3.12.6](https://www.python.org/downloads/release/python-3126/) 」をブラウザで開きます。
以下をダウンロードして実行し、Pythonをインストールします。

- [macOS 64-bit universal2 installer](https://www.python.org/ftp/python/3.12.6/python-3.12.6-macos11.pkg)

詳しくはPythonの公式ドキュメントの「 [Using Python on a Mac](https://docs.python.org/ja/3/using/mac.html) 」を参考にしてください。

インストールが完了したらPythonのバージョンが3.12.6になっていることを確認します（{numref}`check-version-mac`）。

(check-version-mac)=

```{code-block} bash
:caption: Pythonのバージョンを確認

$ python3 -V
Python 3.12.6
```

```{index} single: Install; Windows
```

### Windowsの場合

WindowsでPythonを利用する場合は、Pythonの公式サイトで配布されているWindowsインストーラーを利用します。

「 [Python Release Python 3.12.6](https://www.python.org/downloads/release/python-3126/) 」をブラウザで開きます。
OSによって以下のいずれかのインストーラーをダウンロードし、ウィザードに従ってインストールします。

- 64ビット版: [Windows installer (64-bit)](https://www.python.org/ftp/python/3.12.6/python-3.12.6-amd64.exe)
- 32ビット版: [Windows installer (32-bit)](https://www.python.org/ftp/python/3.12.6/python-3.12.6.exe)

この時、「Add python.exe to PATH」にチェックを入れておきましょう。自動的に必要な環境変数が設定されます（{numref}`windows-install`）。

(windows-install)=

```{figure} images/pythonforwindows1.png
:width: 600

Python for Windowsのインストール画面
```

```{index} single: Install; Linux
```

インストールが完了したらPythonのバージョンが3.12.6になっていることを確認します（{numref}`check-version-win`）。

(check-version-win)=

```{code-block} doscon
:caption: Pythonのバージョンを確認

C:\Users\user>python -V
Python 3.12.6
```

### Linux（Ubuntu Server）の場合

Ubuntu 24.04にはデフォルトでPython 3.12がインストールされています。

以下のコマンドでPythonのバージョンを確認します（{numref}`check-version`）。

(check-version)=

```{code-block} bash
:caption: Pythonのバージョンを確認

$ python3 -V
Python 3.12.3
```

## 注意事項

これ以降の本テキストでは上記手順でインストールしたPython 3.12を使用することを前提に記載しています。

Python 2.7等のPython 2系やAnacondaでインストールしたPython、または [Jupyter](https://jupyter.org/) や [Google Colaboratory](https://colab.research.google.com/?hl=ja) では実習ができません。

Pythonを起動した時に表示される文字をチェックして、下記が問題ないか確認してください。

- Pythonのバージョン(3.10以降を推奨、3.12で説明します)
- Anacondaという文字が表示されないこと

インストールされていない場合は前述の手順でPython 3.12.6のインストールを行ってください。

## まとめ

本節では、事前準備としてエディタ、コマンドラインとPython のインストール方法を紹介しました。
次節ではFizzBuzzを通じたPythonの特徴、基本、役立つWeb の情報、書籍を紹介します。
