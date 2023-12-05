try:
    import openai
except:
    print("ライブラリがインポートできませんでした。プログラムを終了します。")
    exit()

# APIキーを設定
openai.api_key = input('OpenAIのAPIキーを入力してください:')
file_path = input('ファイルパスを教えてください（ファイル名を除く）：')

# チューニングデータをアップロード
file_response = openai.File.create(
  file=open(f"{file_path}/TuningData.jsonl", "rb"),
  purpose='fine-tune'
)
file_id = file_response['id']

# 学習実行
params = {
    "n_epochs":3 # n_epochs = 3 の場合、学習時間は30分程度
    }

fine_tuning_response = openai.FineTuningJob.create(
  training_file=file_id,
  model="gpt-3.5-turbo",
  hyperparameters=params
)
job_id = fine_tuning_response['id']

# ジョブIDを出力
print(f"Job ID: {job_id}")
