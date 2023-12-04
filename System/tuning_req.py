try:
    import openai
except:
    print("ライブラリ:openaiがインストールされていません。インストールします。")
    !pip install openai
    import openai

# チューニングデータをアップロード
file_response = openai.File.create(
  file=open("TuningData.jsonl", "rb"),
  purpose='fine-tune'
)
file_id = file_response['id']

# 学習実行
params = {
    "n_epochs":10
    }

fine_tuning_response = openai.FineTuningJob.create(
  training_file=file_id,
  model="gpt-3.5-turbo",
  hyperparameters=params
)
job_id = fine_tuning_response['id']

# ジョブIDを出力
print(f"Job ID: {job_id}")
