# python-test

## 概要
FastAPI + Docker + Supabase連携のテスト用リポジトリです。
Docker + FastAPI + Supabaseの環境構築が行えたかを確認できます。

## 主な構成
- `app/`
  - `app.py`：FastAPIアプリ本体
  - `supabase_test.py`：Supabase連携テストコード
  - `requirements.txt`：必要なPythonライブラリ一覧
- `Dockerfile`：Python環境・ライブラリのセットアップ
- `docker-compose.yml`：開発用コンテナ管理

## セットアップ手順

1. **リポジトリをクローン**
   ```bash
   git clone https://github.com/opatu07/python-backend-test.git
   cd python-test
   ```

2. **Docker環境の構築・起動**
   ```bash
   docker compose build
   docker compose up -d
   ```

3. **FastAPIのポート確認方法**

1. コンテナ起動後、ブラウザで以下にアクセスしてください：
   - アプリ本体: [http://localhost:8888/](http://localhost:8888/)
   - APIドキュメント: [http://localhost:8888/docs](http://localhost:8888/docs)

2. 表示されれば、FastAPIが正しく設定したポートで動作しています。

3. 表示されない場合は、
   - コンテナが起動しているか（`docker compose ps`で確認）
   - ポート番号の設定ミスがないか
   - ファイアウォールや他のアプリがポートを塞いでいないか

を確認してください。

4. **環境変数（Supabase）の設定**
   ```bash
   cp .env.example .env
   # エディタで .env を開き、自分の SUPABASE_URL / SUPABASE_ANON_KEY を設定
   # 必要なら SUPABASE_TEST_TABLE も指定
   docker compose restart python
   ```

5. **仮想環境（コンテナ）に入る**
   ```bash
   docker compose exec python bash
   ```

6. **Supabase連携テスト**
   ```bash
   python supabase_test.py
   ```

## 注意事項

## ライセンス
MIT
