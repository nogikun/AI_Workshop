from flask_ngrok import run_with_ngrok
from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import pandas as pd
import mysql.connector
import time

# 実行を１分間停止（他のコンテナの起動を待つ）
time.sleep(60)

# データベース接続設定
config = {
  'user': 'server',     # ここにユーザー名を入れます
  'password': 'serverpass', # ここにパスワードを入れます
  'host': 'mysql-db',    # ここにホストを入れます
  'database': 'AI_Workshop_Management', # ここにデータベース名を入れます
  'raise_on_warnings': True
}

# データベースに接続
cnx = mysql.connector.connect(**config)

# SQLクエリを実行し、結果をデータフレームに格納
query = "SELECT * FROM Model" # ここにクエリを入れます
IDtoModel = pd.read_sql(query, cnx)
cnx.close()

# データフレームを表示
print(IDtoModel)

# Flaskの設定
app = Flask(__name__)
run_with_ngrok(app)

@app.route('/get_text', methods=['GET'])
def get_text():
    # 読み込み（MySQLへ通信）
    cnx = mysql.connector.connect(**config)
    IDtoModel = pd.read_sql(query, cnx)
    cnx.close()
    # データフレームを表示
    print(IDtoModel)

    # GETリクエストのパラメータから数値を取得
    get_ID = int(request.args.get('number'))
    print(f'受け取った値：{get_ID}, {type(get_ID)}')
    # GETリクエストのパラメータからテキストデータを取得
    # text_param = request.args.get('text')

    # text_param = check_Status()
    # text_param = 'ft:gpt-3.5-turbo-0613:personal::8ClADDQz'
    text_param = IDtoModel[IDtoModel['ID'] == get_ID]['ModelName'][IDtoModel[IDtoModel['ID'] == get_ID]['ModelName'].index[0]]

    #print(f'({text_param},{type(text_param)})==({np.nan},{type(np.nan)})')
    if str(text_param) == 'nan':
      print('Model名が見つかりませんでした。')
      text_param = 'gpt-3.5-turbo-0613'
      
    print(f'送信した値：{text_param}')

    if text_param:
        # テキストデータを送信元に返す
        return jsonify({'message': f'{text_param}'}), 200
    else:
        return jsonify({'message': 'Text parameter is missing'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    #app.run()

print('SERVER STOPPED')