# ｽﾀｯｸﾁｬﾝのファームウェアについて

### 謝辞
---

[robot8080様のソースコード](https://github.com/robo8080/AI_StackChan2/)を一部改変し使用させていただきました。ここに感謝いたします。

#### 改変したコードについて

以下のファイルについて変更を加えました。
- [./M5Unified_AI_StackChan/src/main.cpp](https://github.com/nogikun/AI_Workshop/blob/main/stackchan/Firmware/M5Unified_AI_StackChan/src/main.cpp)
<br>
また以下の図のように、編集点には以下のコメントを記載しています。

```
///////////////////
//    nogikun    //

{ -- 編集したコード -- }

//      end      //
///////////////////
```

一例：
![image](https://github.com/nogikun/AI_Workshop/assets/94681885/7c90cb55-eef5-49dd-be31-bd7a587f45b3)


### ファームウェア書き出し方法
---

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


<br>

#### 1. プロジェクトを読み込む
---
まずVSCodeで`M5Unified_AI_StackChan`を開く


![image](https://github.com/nogikun/AI_Workshop/assets/94681885/a82bb575-3cf2-48a6-af7d-b1cdf2145a25)



このような見た目になっていたらOK
赤枠 ･･･ PlatFormIOが`platformio.ini`を読み込んでいる場合この用に表示される。

![image](https://github.com/nogikun/AI_Workshop/assets/94681885/79880046-acc3-4271-bd3f-e457a3d0cebc)

![image](https://github.com/nogikun/AI_Workshop/assets/94681885/304c8351-60b2-4656-9d68-35fc5989bd36)


<br>

#### 2. プロジェクトを書き出す
---
下記設定のもと、書き出しボタンを押す！
![image](https://github.com/nogikun/AI_Workshop/assets/94681885/1a975637-f618-4252-9764-ecfdf8ed4967)


ターミナルがこうなっていたらOK！
![image](https://github.com/nogikun/AI_Workshop/assets/94681885/13333eb1-49d7-4753-b57b-df7e6f2708d9)


<br>

#### 補足
---
以下内容は補足資料です。

##### PlatformIOで必要なライブラリのインストール方法

<p style='color:red'>※ まずインストール時にはVSCodeでプロジェクトを開いている必要があります。</p>

赤丸 ⭕ で記されたアイコンをクリックし、`QUICK ACCESS/PIO HOME/Open` より次次の画像を表示できる。
![image](https://github.com/nogikun/AI_Workshop/assets/94681885/962d33ee-2619-4bee-bff5-4cd0904a314f)


`Libraries`をクリックしライブラリの検索をする事ができる。
検索ボックスに`Core2`と入力し、検索を実行する。
![image](https://github.com/nogikun/AI_Workshop/assets/94681885/63376286-2cdd-463a-94cf-8d9183049b56)


検索に以下の内容がヒットはずです。
※ 少しスクロールする必要があります。
![image](https://github.com/nogikun/AI_Workshop/assets/94681885/b5c86166-045e-4b44-b284-b6d06220abc2)


<br>

``Add to Project``ボタンを押し、`Select a project`からプロジェクトのパスを指定し、インストールを行う。
![](https://hackmd.io/_uploads/SydJ4HRWp.png)

![](https://hackmd.io/_uploads/HkDHErR-p.png)
