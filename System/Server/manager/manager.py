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