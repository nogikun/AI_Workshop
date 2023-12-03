# サーバーの使用方法

## サーバーの起動方法

コマンドプロンプトやターミナルで `AI_WORKSHOP/System/Server` へ移動し、以下のコマンドを実行することでサーバーを起動することができます。

```bash
docker-compose up
```

## サーバーの停止方法
コマンドプロンプトに対して `Control + C` を入力することでDocker-composeを停止することができます。
DockerImageごと削除したい場合は以下のコマンドを実行してください。

```bash
docker-compose down --rmi all
```