# Pythonのデータ型（コレクション編）

```{admonition} 節サブタイトル
データ型をまとめるコレクションの紹介
```

```{index} Collection
```

Pythonのデータ型のうち、複数のデータ型をひとまとめにして扱えるコレクションを紹介します。

## はじめに

本節では次の4つを扱います。リスト（`list`）、タプル（`tuple`）、辞書（`dict`）と集合（`set`）を扱います。

```{index} list single: Collection; list
```

## リスト（list）

リストはコレクションの1つです。複数の型のデータをひとまとめにできます。

リストを定義するには角括弧（`[ ]`）を使い、含める要素をカンマ（`,`）で区切ります（{numref}`define-list`）。

(define-list)=

```{code-block} pycon
:caption: "リストの定義"

>>> ['spam', 'egg', 0.5]
['spam', 'egg', 0.5]
```

リストも文字列と同様に、結合やスライスが使えます（{numref}`use-list`）。

(use-list)=

```{code-block} pycon
:caption: "リストの基本的な使い方"

>>> ['spam', 'ham'] + ['egg']              # リストの結合
['spam', 'ham', 'egg']
>>> ['spam'] * 5                           # リストの繰り返し
['spam', 'spam', 'spam', 'spam', 'spam']
>>> ['spam', 'ham', 'egg'][0]              # リストの0番目を取得する
'spam'
>>> ['spam', 'ham', 'egg'][1:]             # リストのスライス(1番目以降)
['ham', 'egg']
>>> len(['spam', 'ham', 'egg'])            # リストの長さ
3
>>> 'ham' in ['spam', 'ham', 'egg']        # リストに特定の文字列が含まれるか
True
```

```{index} for single: Collection; for
```

### for文

リストは、 `for` 文の繰り返し用変数として使えます（{numref}`for-list`）。

(for-list)=

```{code-block} pycon
:caption: "for文とリスト"

>>> for animal in ['cat', 'dog', 'snake']:
...     print(animal)
...
cat
dog
snake
```

```{hint}
[listのfor文での繰り返し動作を確認](https://pythontutor.com/render.html#code=for%20animal%20in%20%5B'cat',%20'dog',%20'snake'%5D%3A%0A%20%20%20%20print%28animal%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false)

<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=for%20animal%20in%20%5B'cat',%20'dog',%20'snake'%5D%3A%0A%20%20%20%20print%28animal%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>
```

```{index} append() single: Collection; append()
```

### 要素の追加

リストに要素を追加するには、 `.append()` メソッドを使います。
`.append()` メソッドはリストの末尾に要素を追加します（{numref}`list-append`）。

(list-append)=

```{code-block} pycon
:caption: "リストへの要素追加"

>>> animals = ['cat', 'dog', 'snake']
>>> animals.append('elephant')
>>> animals
['cat', 'dog', 'snake', 'elephant']
```

リストは変更可能なオブジェクトです。
`.append()` メソッドによって、 `animals` というリストの内容が変更されます。

```{hint}
[listへの要素の追加の動作を確認](https://pythontutor.com/render.html#code=animals%20%3D%20%5B'cat',%20'dog',%20'snake'%5D%0Aanimals.append%28'elephant'%29%0Aprint%28animals%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false)

<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=animals%20%3D%20%5B'cat',%20'dog',%20'snake'%5D%0Aanimals.append%28'elephant'%29%0Aprint%28animals%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>
```

```{index} comprehension single: Collection; comprehension
```

### リスト内包表記

リスト内包表記はリストの定義方法の1つです。
比較的複雑なリストの定義を、シンプルに記述できます。

`for` 文の例として `animals` リストから各文字列の長さの一覧を作ります（{numref}`general-for`）。

(general-for)=

```{code-block} pycon
:caption: "一般的なfor文"

>>> ret = []
>>> for animal in animals:
...     ret.append(len(animal))
...
>>> ret
[3, 3, 5, 8]
```

{numref}`general-for` をリスト内包表記に置き換えると、 {numref}`list-comprehension` のようになります。

(list-comprehension)=

```{code-block} pycon
:caption: "リスト内包表記"

>>> [len(animal) for animal in animals]
[3, 3, 5, 8]
```

3行で記述していたコードが1行になりました。内包表記を使うと簡潔に記述できることがわかったと思います。
最初は見慣れないかもしれませんが、徐々に慣れていくと良いと思います。

リストの定義時に、角括弧（`[ ]`）の内部に `for` を書きます。
`for ＜変数名＞ in` の部分は通常の `for` 文と同じです。

`for` の左側でひとつひとつ取り出した要素（ここでは `animal`）を使い、リストの各要素を作ります。 {numref}`list-comprehension` の場合、 `len(animal)` の結果が各要素になります。

リスト内包表記は、条件文や複数回のループ処理も記述できます。
複雑にしすぎると、かえって可読性を落としますので、ほどほどに使用することをおすすめします。複雑になりすぎる場合はループ処理で書きましょう。
リスト内包表記の仲間に、辞書(後述)を生成する辞書内包表記や、セット(後述)を生成するセット内包表記やジェネレータ式(本チュートリアルでは取り扱わない)などもあります。
内包表記はPythonの強力な機能の1つなのでぜひ覚えておくとよいでしょう。

他にも役に立つ書き方があるので、Pythonのドキュメントを参考にしてください。

- リストの内包表記 <https://docs.python.org/ja/3/tutorial/datastructures.html#list-comprehensions>

```{index} substitute single: Collection; substitute
```

### 複数変数への代入

リストのようなシーケンス型から他のデータ型に値を代入する際、複数の変数への代入を一度に行えます（{numref}`multi-substitute`）。

(multi-substitute)=

```{code-block} pycon
:caption: "シーケンス型から複数変数への代入"

>>> dog, cat = ['dog', 'cat']
>>> dog
'dog'
>>> cat
'cat'
```

複数の変数への代入は、右辺が文字列や後述するタプルの場合でも可能です。

```{index} tuple single: Collection; tuple
```


## 辞書（dict）

辞書はリストと同じコレクションです。

辞書の各要素はキー（key）と、対応する値（value）を持ち、Python 3.7 以降では要素の挿入順が保持されます。

辞書を定義するには波括弧（`{}`）で各要素を囲み、コロン（`:`）でキーと値を書きます（{numref}`guide-dict`）。
値と次のキーの間はカンマ（`,`）で区切ります。

(guide-dict)=

```{code-block} pycon
:caption: "辞書"

>>> user_info = {'user_name': 'taro', 'last_name': 'Yamada'}
>>> user_info
{'user_name': 'taro', 'last_name': 'Yamada'}
```

{numref}`guide-dict` の `user_info` から `'user_name'` の値を取り出す処理は、 {numref}`get-dict-value` になります。

(get-dict-value)=

```{code-block} pycon
:caption: "辞書からの値の取り出し"

>>> user_info['user_name']
'taro'
```

既存の辞書に値を設定するには、 `辞書[＜キー＞]` に直接代入します（{numref}`set-dict-value`）。

(set-dict-value)=

```{code-block} pycon
:caption: "辞書への値の設定"

>>> user_info['first_name'] = 'Taro'
>>> user_info
{'user_name': 'taro', 'last_name': 'Yamada', 'first_name': 'Taro'}
```

```{index} in single: Collection; in
```

### in演算子

辞書内にキーが存在しているかどうかを調べるには、 `in` 演算子を使います（{numref}`dict-in`）。

(dict-in)=

```{code-block} pycon
:caption: "辞書のin"

>>> 'user_name' in user_info
True
>>> 'bio' in user_info
False
```

```{index} get() single: Collection; get()
```

### .get()メソッド

辞書から値を取得するときに、キーが存在しない場合はエラー(KeyError)になります（{numref}`dict-keyerror`）。

(dict-keyerror)=

```{code-block} pycon
:caption: "存在しないキーの参照"

>>> user_info['bio']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'bio'
```

`.get()` メソッドで取得すると、キーが存在しない場合には `None` が返されます（  {numref}`get-from-dict`）。

(get-from-dict)=

```{code-block} pycon
:caption: "存在しないキーへのget"

>>> user_info.get('user_name')
'taro'
>>> bio = user_info.get('bio')
>>> print(bio)
None
```

`None` は、Pythonの組み込み定数の1つで、何も値がないことを表します。

インタープリタは `None` を表示しないので、明示的に `print()` 関数を使っています。

値が存在しないときに `None` 以外の値を返したい場合には、 `.get()` メソッドの第2引数に返したい値を指定します。
`'bio'` の値が取れない場合に空文字列（`''`）としたい場合は、 {numref}`get-with-default` のように書きます。

(get-with-default)=

```{code-block} pycon
:caption: "デフォルト値付きのget"

>>> user_info.get('bio', '')
''
```

```{index} for() single: Collection; for()
```

### for文

辞書を `for` 文の繰り返し用変数として使用すると、変数にはキーが入ります({numref}`dict-for`)。

(dict-for)=

```{code-block} pycon
:caption: "辞書を使用したfor文"

>>> user_info = {'user_name': 'taro', 'last_name': 'Yamada'}
>>> for key in user_info:
...     print(key)
...     print(user_info[key])
...
user_name
taro
last_name
Yamada
```

```{hint}
[辞書のfor文の動作を確認](https://pythontutor.com/render.html#code=user_info%20%3D%20%7B'user_name'%3A%20'taro',%20'last_name'%3A%20'Yamada'%7D%0Afor%20key%20in%20user_info%3A%0A%20%20%20%20print%28key%29%0A%20%20%20%20print%28user_info%5Bkey%5D%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false)

<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=user_info%20%3D%20%7B'user_name'%3A%20'taro',%20'last_name'%3A%20'Yamada'%7D%0Afor%20key%20in%20user_info%3A%0A%20%20%20%20print%28key%29%0A%20%20%20%20print%28user_info%5Bkey%5D%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>
```

### .keys()メソッド、.values()メソッド、.items()メソッド

すべてのキー、値の要素をリストで取得するには、 `.keys()` 、 `.values()` 、 `.items()` メソッドを使います。

- `.keys()`: すべてのキーを取得
- `.values()`: すべての値を取得
- `.items()`: すべてのキーと値を、要素が2つのタプルで取得

たとえば、辞書内のすべてのキーと値を取得するには、 {numref}`get-all-items` のようにします。

(get-all-items)=

```{code-block} pycon
:caption: "辞書内のすべてのキーと値を取得"

>>> d = {'foo': 'spam', 'bar': 'ham'}
>>> d.items()
dict_items([('foo', 'spam'), ('bar', 'ham')])
```

`.items()` の結果を `for` 文に渡せば、辞書内のすべての値を使った繰り返し処理を書けます。

`for` 文の変数名を2つ指定することで、要素が2つのタプルからキーと値をそれぞれの変数に一度で受け取れます（{numref}`for-with-dict-items`）。

(for-with-dict-items)=

```{code-block} pycon
:caption: "for文で辞書のキーと値を使う"

>>> d = {'foo': 'spam', 'bar': 'ham'}
>>> for key, value in d.items():
...     print(key, value)
...
foo spam
bar ham
```

各メソッドの戻り値はイテレータブルオブジェクトです。

```{admonition} コラム: イテレータブルオブジェクト
`.keys()` 、 `.values()` 、 `.items()` の戻り値の型はリストやタプルではなくそれぞれ `dict_keys` 、 `dict_values`、 `dict_items` ですが、いずれも `for` 文でデータを取り出すことができます。Pythonの `for` 文は、「イテレータブルオブジェクト」という連続したデータ構造を表すオブジェクトであれば扱えるため、このような動きになります。
```

```{index} set single: Collection; set
```

## タプル（tuple）

タプルもリスト、辞書と同じコレクションの1つです。

タプルを定義するには括弧（`( )`）を使い、含める要素をカンマ（`,`）で区切ります（{numref}`define-tuple`）。

(define-tuple)=

```{code-block} pycon
:caption: "タプルの定義"

>>> ('spam', 'ham', 4)
('spam', 'ham', 4)
```

タプルもリスト、文字列と同様に、結合やスライスが使えます（{numref}`use-tuple`）。

(use-tuple)=

```{code-block} pycon
:caption: "タプルの基本的な使い方"

>>> ('spam', 'ham') + ('egg',)             # タプルの結合
('spam', 'ham', 'egg')
>>> ('spam',) * 5                          # タプルの繰り返し
('spam', 'spam', 'spam', 'spam', 'spam')
>>> ('spam', 'ham', 'egg')[0]              # タプルの0番目を取得する
'spam'
>>> ('spam', 'ham', 'egg')[1:]             # タプルのスライス(1番目以降)
('ham', 'egg')
>>> len(('spam', 'ham', 'egg'))            # タプルの長さ
3
>>> 'ham' in ('spam', 'ham', 'egg')        # タプルに特定の文字列が含まれるか
True
```

要素が1つのタプルを定義する際にもカンマが必要な点に注意してください。
これは、処理の優先順位を決める括弧と区別するためです（{numref}`single-tuple`）。

(single-tuple)=

```{code-block} pycon
:caption: "1要素のタプル"

>>> ('spam',)
('spam',)
>>> ('spam')
'spam'
```

また、括弧を省略してタプルを定義できます（{numref}`omit-parenthesis-tuple`）。

(omit-parenthesis-tuple)=

```{code-block} pycon
:caption: "括弧を省略したタプル"

>>> 'dog', 'cat'
('dog', 'cat')
```

```{index} immutable single: Collection; immutable
```

### リストとの違いと使いどころ

リストと違いタプルは不変（immutable）な値です。
リストの `.append()` のような破壊的な操作は存在しません。
`.append()` のような処理を行いたい場合は、タプルの結合により新しいタプルを作るしかありません。

タプルは、関数の戻り値や不変としたい設定用の値に使います。

関数からタプルを返すと、簡単に複数の値を戻り値として返すことができます。

シーケンス（リスト、タプルや文字列）を受け取り、初めの要素と残りの要素に分割する関数を、 {numref}`return-tuple` に示します。

(return-tuple)=

```{code-block} pycon
:caption: "タプルを返す関数"

>>> def head_splitter(seq):
...     return seq[0], seq[1:]
...
>>> head, tail = head_splitter(['head', 'body', 'tail'])
>>> head
'head'
>>> tail
['body', 'tail']
```

戻り値の順番に意味が必要になるため、要素の多いタプルを返すのは避けましょう（{numref}`many-return-value`）。

(many-return-value)=

```{code-block} pycon
:caption: "要素数の多いタプルを返す関数"

>>> def bad_implementation():
...     return 'username', 'user_password', 'user_id', 'user_permission1', 'user_permission2'
...
>>> username, user_password, user_id, user_permission1, user_permission2 = bad_implementation()
```

{ref}`many-return-value` のような場合、辞書（後述）、専用のクラスのインスタンス、名前付きタプルなどで返しましょう
（クラスの定義方法、名前付きタプルについては、本チュートリアルでは説明しません）。  

```{admonition} コラム: 辞書のキーとしてタプルを使用する （リストは辞書のキーで利用不可）
タプルが辞書のキーとして便利な理由は、その不変性と複数の値をひとつのエントリとして扱える特性です。この性質を利用することで、複数の関連したデータの組み合わせを辞書のキーとして使うことができます。

タプルを辞書のキーとして使う例

    >>> color_map = {
    ...     (0, 0): "red",
    ...     (1, 0): "green",
    ...     (0, 1): "blue"
    ... }
    >>>
    >>> color_map[(1, 0)]
    'green'

上記の実行例のようにタプルは不変なデータ型なので辞書のキーとして使えます。

一方でリストは変更可能なデータ型なので辞書のキーに使うことはできません。

リストを辞書のキーとして使う例（エラー）

    >>> color_map = {
    ...     [0, 0]: "red",
    ...     [1, 0]: "green",
    ...     [0, 1]: "blue"
    ... }

リストを辞書のキーとして使用した際に出力されるエラー

    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unhashable type: 'list'

このエラーは、リストの可変性が問題となることを示しており、タプルの不変性が辞書のキーとして使われる際の重要な特徴であることを理解するのに役立ちます。
```

```{index} dict single: Collection; dict
```
## 集合（set）

集合型（set）はコレクション型の1つです。

リストやタプルのように値しか持ちませんが、順序も持ちません。

1つの集合内には同じ値が1つしか存在できません。そのため、一意な値を管理する際に非常に役立ちます。

ただし、辞書のキーと同じように、集合内には不変の値しか持てません。

集合は波括弧（`{ }`）で囲んだ中に、要素をカンマ（`,`）で区切って指定して定義します（{numref}`define-set`）。

(define-set)=

```{code-block} pycon
:caption: "集合の定義"

>>> {'spam', 'ham'}
{'spam', 'ham'}
>>> {'spam', 'spam', 'spam'}
{'spam'}
```

```{index} add() single: Collection; add()
```

### .add()メソッド

集合に要素を追加するには `.add()` メソッドを使います。
追加したい要素を引数に渡して呼び出します（{numref}`set-add-method`）。

(set-add-method)=

```{code-block} pycon
:caption: "集合への要素の追加"

>>> unique_users = {'dog', 'cat'}
>>> unique_users.add('snake')
>>> unique_users
{'dog', 'cat', 'snake'}
```

集合の要素数も `len()` 関数で取得できます（{numref}`len-with-set`）。

(len-with-set)=

```{code-block} pycon
:caption: "集合によるユニーク数管理"

>>> len(unique_users)
3
>>> unique_users.add('snake')
>>> unique_users.add('snake')
>>> unique_users.add('snake')
>>> len(unique_users)
3
```

{numref}`len-with-set` で要素が2つの `unique_users` という集合を定義し、後に要素を追加しています。
ここで `unique_users` の要素数は3です。
{numref}`len-with-set` では、集合内にすでに存在する `'snake'` という要素を `.add()` で3 回追加していますが、 `len()` 関数の結果は変わりません。

このように、集合では一意な値が適切に管理されていることがわかります。

```{index} product single: Collection; product
```

### 集合の積と和

2つの集合から集合の積を取り、両方の集合に存在する要素の集合を取得できます。

この場合、2つの集合に対してAND（`&`）演算子を使います（{numref}`product-of-sets`）。

(product-of-sets)=

```{code-block} pycon
:caption: "2集合の積"

>>> allowed_permissions = {'edit', 'view'}
>>> requested_permissions = {'view', 'delete'}
>>> allowed_permissions & requested_permissions
{'view'}
```

{numref}`product-of-sets` では、アプリケーションから許可された権限の一覧 `allowed_permissions` を使って、ユーザに要求された権限 `requested_permissions` のフィルタリングを行う状況を想定しています。
結果としてユーザに許可された権限は `'view'` のみとなりました。

```{index} sum single: Collection; sum
```

集合の和も取得できます。
両方の集合を合わせた集合を取得できます。
2つの集合に対してOR（`¦`）演算子を使います（{numref}`sum-of-sets`）。

(sum-of-sets)=

```{code-block} pycon
:caption: "2つの集合の和"

>>> editor = {'edit', 'comment'}
>>> reviewer = {'comment', 'approve'}
>>> editor | reviewer
{'comment', 'approve', 'edit'}
```

{numref}`sum-of-sets` では、`editor` と `reviewer` はロール（役割）を想定しています。
この2つのロールを持つユーザは、`'edit'`、`'comment'` と `'approve'` の権限を持つことを算出しました。

## まとめ

データ型をひとまとめにして扱えるコレクションを紹介しました。
実現したいことに合わせたコレクションを選択しましょう。
