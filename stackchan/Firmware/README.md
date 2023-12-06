# ｽﾀｯｸﾁｬﾝのファームウェアについて

### 謝辞
[robot8080様のソースコード](https://github.com/robo8080/AI_StackChan2/)を一部改変し使用させていただきました。ここに感謝いたします。

#### 改変したコードについて
以下の図のように、編集点には以下のコメントを記載しています。

```
///////////////////
//    nogikun    //

{ 編集したコード }

//      end      //
///////////////////
```

### 書き出し方法

#### 使用したソフトウェア
- VSCode ( Visual Studio Code )
    - [こちら](https://code.visualstudio.com/download)からDLできます。

##### VSCodeで必要な拡張機能
|拡張機能|説明|
|:-:|:-:|
|PlatformIO|マイコンにファームウェアを書き込むことやプログラムの検証ができる。|

##### PlatformIOで必要なライブラリ

|ライブラリ|説明|
|:-:|:-:|
|M5Core2|M5Stack Core2の書き出し用ライブラリ|
|M5GFX|M5Stackシリーズ用開発ライブラリ|
|M5Unified|M5Stackシリーズ用開発ライブラリ|

※ 適応方法は [こちら](#PlatformIOで必要なライブラリのインストール方法) に記載しています。




#### 1. プロジェクトを読み込む
まずVSCodeで`M5Unified_AI_StackChan`を開く


![](https://hackmd.io/_uploads/S13THvCZa.png)


このような見た目になっていたらOK
赤枠 ･･･ PlatFormIOが`platformio.ini`を読み込んでいる場合この用に表示される。

![](https://hackmd.io/_uploads/By9KtwAWp.png)



#### 2. プロジェクトを書き出す
下記設定のもと、書き出しボタンを押す！
![](https://hackmd.io/_uploads/ryAbhDRZp.png)

ターミナルがこうなっていたらOK！
![](https://hackmd.io/_uploads/B1C2hvAZT.png)



#### 補足
以下内容は補足資料です。

##### PlatformIOで必要なライブラリのインストール方法

<p style='color:red'>※ まずインストール時にはVSCodeでプロジェクトを開いている必要があります。</p>

赤丸 ⭕ で記されたアイコンをクリックし、`QUICK ACCESS/PIO HOME/Open` より次次の画像を表示できる。
![](https://hackmd.io/_uploads/HJ75-SRbT.png)

`Libraries`をクリックしライブラリの検索をする事ができる。
検索ボックスに`Core2`と入力し、検索を実行する。
![](https://hackmd.io/_uploads/BJI2a4Aba.png)

検索に以下の内容がヒットはずです。
※ 少しスクロールする必要があります。
![](https://hackmd.io/_uploads/rJu8oE0bT.png)

<br>

``Add to Project``ボタンを押し、`Select a project`からプロジェクトのパスを指定し、インストールを行う。
![](https://hackmd.io/_uploads/SydJ4HRWp.png)

![](https://hackmd.io/_uploads/HkDHErR-p.png)