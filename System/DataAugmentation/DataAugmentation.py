import pandas as pd
import json

file_path = input('ファイルパスを教えてください（ファイル名を除く）：')
DATA = pd.read_excel(f'{file_path}/FineTuningData.xlsx') # ファイル名は適宜変更する。

add_num = int(input('何個の文を追加しますか？（数字のみ）：'))
for i in range(len(DATA['user'])):
  for j in range(add_num):
    new_data = pd.DataFrame([{
        'system':DATA['system'][i],
        'user':DATA['user'][i], # 書き換えた入力を加える
        'assistant':DATA['assistant'][i]
        }])
    DATA = pd.concat([DATA, new_data], ignore_index=True)


# チューニングデータを作成
TunigData = []
for i in DATA.T:
  append_json = {
      'messages': [
          {'role': 'system','content': DATA.T[i]['system']},
           {'role': 'user', 'content': DATA.T[i]['user']},
            {'role': 'assistant','content': DATA.T[i]['assistant']}
      ]}
  TunigData.append(append_json)

with open(f'{file_path}/TuningData.jsonl', 'w') as file:
  for entry in TunigData:
      file.write(json.dumps(entry) + '\n')

print(f'学習用ファイルを作成しました。\nファイルパス:{file_path}/TuningData.jsonl')
print(DATA)