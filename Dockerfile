FROM python:3.11

# 作業ディレクトリを設定 cmdなどを実行するディレクトリを指定
WORKDIR /app

# gitをインストール
RUN apt-get update && apt-get install -y git

# 依存ライブラリをインストール
## requirements.txtをコンテナ内appにコピー
COPY requirements.txt .
## 依存ライブラリをインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリ本体をコピー
COPY . .

# FastAPIを起動（デバッグ用）
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
