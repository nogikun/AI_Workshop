# ライブラリのインポート
try:
    import numpy as np
    import pandas as pd
    import json
    import torch
    import sentencepiece
    import MeCab
    import unidic
    import ipadic
    from transformers import pipeline
    from transformers import AutoTokenizer, AutoModelForMaskedLM
except:
    print("ライブラリがインポートできませんでした。プログラムを終了します。")
    exit()

# BERTモデルのインスタンス化
pipe = pipeline("fill-mask", model="nlp-waseda/roberta-base-japanese")
tokenizer = AutoTokenizer.from_pretrained("nlp-waseda/roberta-base-japanese")
model = AutoModelForMaskedLM.from_pretrained("nlp-waseda/roberta-base-japanese")


#
# 関数定義
#

# 分かち書きを行う関数
def wakachi(text = '早稲田大学で自然言語処理を専攻する。'): # 引数に入っている初期値は想定する入力
  # 分かち書き
  DATA = np.array([['','']])
  mecab = MeCab.Tagger(ipadic.MECAB_ARGS)
  tokens = mecab.parse(text)

  for token in tokens.split('\n'):
    data = token.split('\t')
    try:
      # print([[data[0],data[1].split(',')[0]]])
      DATA = np.append(DATA, [[data[0],data[1].split(',')[0]]],0)
    except:
      pass
  DATA=DATA[1:]

  texts = []
  for i in range(len(DATA.T[0])):
    if DATA.T[1][i] in ['名詞']:
      texts.append(' '.join(list(DATA.T[0][:i])+['[MASK]']+list(DATA.T[0][i+1:])))
  return texts

# BERTによる予測を行う関数
def word_prediction(text = "早稲田 大学 で 自然 言語 処理 を [MASK] する 。",add_num = 10): # 引数に入っている初期値は想定する入力
  input_ids = tokenizer.encode(text, return_tensors="pt")
  mask_idx = input_ids.tolist()[0].index(tokenizer.mask_token_id)
  with torch.no_grad():
      prediction = model(input_ids).logits

  # Get the probabilities using softmax
  probs = torch.nn.functional.softmax(prediction[0, mask_idx], dim=0)

  # Get the top 10 predicted token ids and their probabilities
  top_10_token_ids = torch.topk(probs, add_num).indices
  top_10_probs = torch.topk(probs, add_num).values

  predicted_words = [tokenizer.decode([token_id]) for token_id in top_10_token_ids]

  # Zip the words with their probabilities and print them
  for word, prob in zip(predicted_words, top_10_probs):
      pass
      #print(f"{word}: {prob.item():.5f}")

  return predicted_words  # zip(predicted_words, top_10_probs)


#
# メイン処理
#  

file_path = input('ファイルパスを教えてください（ファイル名を除く）：')
DATA = pd.read_excel(f'{file_path}/FineTuningData.xlsx') # ファイル名は適宜変更する。

# １文に対して何個の言い換え文を作成するかを決定する
add_num = int(input('一つのワードに対して何個の言い換え文を作成しますか？（数字のみ）：'))

for i in range(len(DATA['user'])):
  # 言い換え文を作成
  new_keywords = []
  for text in wakachi(text = DATA['user'][i]): # userの入力文を与える
    for word in word_prediction(text,add_num):
      if word not in  ['。','、','?','!','.','...','......','−','–','――','「','」','～','(',')','『','”',':']:
        new_keywords.append( text.replace('[MASK]', word).replace(' ', '') )

  # 拡張したデータを追加
  for new_keyword in new_keywords:
    new_data = pd.DataFrame([{
        'system':DATA['system'][i],
        'user':new_keyword, # 書き換えた入力を加える
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