import os
from supabase import create_client, Client


def get_supabase() -> Client:
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_ANON_KEY")
    if not url or not key:
        missing = [name for name, v in {"SUPABASE_URL": url, "SUPABASE_ANON_KEY": key}.items() if not v]
        raise RuntimeError(f"環境変数が未設定です: {', '.join(missing)}. .env に設定してから再実行してください。")
    return create_client(url, key)


def main() -> None:
    supabase = get_supabase()
    table = os.environ.get("SUPABASE_TEST_TABLE", "test_table")
    try:
        response = supabase.table(table).select("*").limit(1).execute()
        print("接続成功！データ:", response.data)
    except Exception as e:
        print("接続失敗:", e)


if __name__ == "__main__":
    main()
