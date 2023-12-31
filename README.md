# AI_Workshop 仕様書
※ お問い合わせの際は、[新しいIssues](https://github.com/nogikun/AI_Workshop/issues/new) を立てて頂けますと幸いです。

**目次**
- [AI\_Workshop 仕様書](#ai_workshop-仕様書)
    - [背景](#背景)
    - [システムの概要](#システムの概要)
    - [1.データセットの拡張](#1データセットの拡張)
    - [2.FineTuning のリクエスト](#2finetuning-のリクエスト)
    - [3.管理サーバー](#3管理サーバー)
    - [4.使用するロボットのファームウェアについて](#4使用するロボットのファームウェアについて)

### 背景
このレポジトリでは小学生向けのAIロボットを用いたワークショップを行うために使用したソースコードをまとめております。

### システムの概要
このシステムは、以下の3つの機能を持つ。
- データセットの拡張
- FineTuning のリクエスト
- 管理サーバー（M5Stackとの通信）

当セクションではそれぞれの機能について解説する。

<br>

### 1.データセットの拡張
---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nogikun/AI_Workshop/blob/main/System/JupyterNotebook/DataAugmentation/DataAugmentation_BERT.ipynb)
<br> ※お手持ちのデバイスがGPUを搭載していない場合は、上記のボタンをクリックしてGoogle Colaboratory上で実行してください。

|ファイル名|概要|実行|
|:-:|:-:|:-:|
|[DataAugmentation_BERT.py](https://github.com/nogikun/AI_Workshop/blob/main/System/DataAugmentation/DataAugmentation_BERT.py)|BERTモデルを使用し、入力データと似た文章を生成し、データ拡張を行うスクリプト|[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nogikun/AI_Workshop/blob/main/System/JupyterNotebook/DataAugmentation/DataAugmentation_BERT.ipynb)|
|[DataAugmentation.py](https://github.com/nogikun/AI_Workshop/blob/main/System/DataAugmentation/DataAugmentation.py)|同一のデータを入力値倍し、データ件数を増やすスクリプト|[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nogikun/AI_Workshop/blob/main/System/JupyterNotebook/DataAugmentation/DataAugmentation.ipynb)|

**データ拡張の遷移図**

![image:データ拡張の遷移図](https://github.com/nogikun/AI_Workshop/assets/94681885/5abc5b69-8039-4e97-ad6b-37b3daebbe3d)

<br>

### 2.FineTuning のリクエスト
---

|ファイル名|概要|実行|
|:-:|:-:|:-:|
|[tuning_req.py](https://github.com/nogikun/AI_Workshop/blob/main/System/tuning_req.py)|OoenAIへGPT3.5モデルのチューニングリクエストを送るスクリプト|[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nogikun/AI_Workshop/blob/main/System/JupyterNotebook/RequestFineTuning/tuning_req.ipynb)|


**モデルの学習フロー**

![image:モデルの学習フロー](https://github.com/nogikun/AI_Workshop/assets/94681885/5f208797-cf69-4b24-adcd-86f37b0f9622)

**学習jobの進捗を確認する方法**

下記リンクのOpenAIのダッシュボードへアクセスし、下図のような学習jobの進捗を確認することができます。<br>
ログインしていない場合は、遷移先でログインを行ってください。<br>
ダッシュボード：[platform.openai.com/finetune](https://platform.openai.com/finetune) 

<img src="https://github.com/nogikun/AI_Workshop/assets/94681885/090e944d-64e4-48a1-b717-c29a8aafd0b1.jpg" width="70%">

<br><br>

また学習完了するとこのようなメールが届き、モデル名が記載されています。このモデル名をデータベースに書き込みます。<br>
※ モデル名は `ft:{Base Model}:pearsonal::{id}` の形式で発行されます。<br><br>
<img src="https://github.com/nogikun/AI_Workshop/assets/94681885/2ecbc256-f8b8-4f2d-96cd-009f65fc0014.jpg" width="50%">


<br>

### 3.管理サーバー
---
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/nogikun/AI_Workshop)
<br> ※クローンせずともCodespaces上で実行することができます。是非お使いください。
<br>　また、サーバの起動方法などは [こちら](https://github.com/nogikun/AI_Workshop/blob/main/System/Server/README.md) を参照してください。
|ファイル名|概要|
|:-:|:-:|
|[stack_server.py](https://github.com/nogikun/AI_Workshop/blob/main/System/Server/stack_server/stack_server.py)|M5Stackと通信を行い、任意のIDに対応する学習済みモデル名を送信するスクリプト<br> ※ Dockerを使用|

**管理サーバーとM5Stack（ｽﾀｯｸﾁｬﾝ）との関係**

![image](https://github.com/nogikun/AI_Workshop/assets/94681885/f8e64570-6e16-43d3-9dd1-b4d21e14d607)

### 4.使用するロボットのファームウェアについて
---

今回、使用するAIロボットは 「 **ｽﾀｯｸﾁｬﾝ** 」 と呼ばれるロボットです。
外装はこの通りとなっております。

**"ｽﾀｯｸﾁｬﾝ"の外装**

<img src="https://github.com/nogikun/AI_Workshop/assets/94681885/0e75a7eb-0c37-43bc-9a92-b8abca8415ff.jpg" width="50%">

<br>

※　ファームウェアの書き出しについては [こちら](https://github.com/nogikun/AI_Workshop/tree/main/stackchan/Firmware) をご参照ください。
