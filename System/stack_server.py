from xlrd.formula import get_cell_addr
file_path = '/content/drive/MyDrive/ロボットストリート2023 - IPUT E-2 (File responses)/System/ID_to_Model.xlsx'

# 起動
server_type = int(input('サーバータイプ：\n・0 ･･･ 10:30~\n・1 ･･･ 13:00~\n---------------------\n入力：')) # 0 ･･･ 10:30~ , 1 ･･･ 13:00~
print(f"// {['10:30~','13:00~'][server_type]} の時間枠用として起動します。//\n") # アナウンス

IDtoModel = pd.read_excel(file_path,sheet_name=server_type)
IDtoModel_sheets = pd.ExcelFile(file_path).sheet_names

from flask_ngrok import run_with_ngrok
from flask import Flask, request, jsonify
from flask_cors import CORS

import numpy as np
import pandas as pd

app = Flask(__name__)
run_with_ngrok(app)

@app.route('/get_text', methods=['GET'])
def get_text():
    # 読み込み
    IDtoModel = pd.read_excel(file_path,sheet_name=server_type)
    IDtoModel_sheets = pd.ExcelFile(file_path).sheet_names

    # GETリクエストのパラメータから数値を取得
    get_ID = int(request.args.get('number'))
    print(f'受け取った値：{get_ID}, {type(get_ID)}')
    # GETリクエストのパラメータからテキストデータを取得
    # text_param = request.args.get('text')

    # text_param = check_Status()
    text_param = 'ft:gpt-3.5-turbo-0613:personal::8ClADDQz'
    text_param = IDtoModel[IDtoModel['StackchanID'] == get_ID]['ModelName'][IDtoModel[IDtoModel['StackchanID'] == get_ID]['ModelName'].index[0]]

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
    #app.run(host='0.0.0.0', port=5000)
    app.run()