# AI_Workshop 仕様書

**目次**
- [AI\_Workshop 仕様書](#ai_workshop-仕様書)
    - [背景](#背景)
    - [システムの概要](#システムの概要)
      - [データセットの拡張](#データセットの拡張)
      - [FineTuning のリクエスト](#finetuning-のリクエスト)
      - [管理サーバー](#管理サーバー)

### 背景
このレポジトリでは小学生向けのAIワークショップを行うために使用したソースコードをまとめております。

### システムの概要
このシステムは、以下の3つの機能を持つ。
- データセットの拡張
- FineTuning のリクエスト
- 管理サーバー（M5Stackとの通信）

当セクションではそれぞれの機能について解説する。

#### データセットの拡張

|ファイル名|概要|
|:-:|:-:|
|[DataAugmentation_BERT.py]()|BERTモデルを使用し、入力データと似た文章を生成し、データ拡張を行うスクリプト|

![image](https://github.com/nogikun/AI_Workshop/assets/94681885/5abc5b69-8039-4e97-ad6b-37b3daebbe3d)

#### FineTuning のリクエスト

|ファイル名|概要|
|:-:|:-:|
|[tuning_req.py]()|OoenAIへGPT3.5モデルのチューニングリクエストを送るスクリプト|

![image](https://github.com/nogikun/AI_Workshop/assets/94681885/5f208797-cf69-4b24-adcd-86f37b0f9622)

#### 管理サーバー

|ファイル名|概要|
|:-:|:-:|
|[stack_server.py]()|M5Stackと通信を行い、任意のIDに対応する学習済みモデル名を送信するスクリプト|

![image](https://github.com/nogikun/AI_Workshop/assets/94681885/09db193e-245d-43d7-8235-06d2d8c342b2)
