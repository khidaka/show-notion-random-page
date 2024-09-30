# Notion Random Page Script

このスクリプトは、Notionデータベースからランダムなページを取得し、ブラウザで表示します。

## 必要条件

- Python 3.x
- `requests`ライブラリ

## インストール

1. **Python環境の準備**:
   Pythonがインストールされていることを確認してください。

2. **ライブラリのインストール**:
   ターミナルで以下のコマンドを実行して、必要なライブラリをインストールします。

   ```bash
   pip install requests
   ```

## 設定ファイルの作成

1. `config.json`ファイルを作成し、以下の内容で保存します。複数の設定ファイルを作成することもできます。

   ```json
   {
       "NOTION_API_KEY": "your_api_key_here",
       "DATABASE_ID": "your_database_id_here"
   }
   ```

## 使用方法

1. スクリプトを実行する際に、設定ファイルを引数として指定します。

   ```bash
   python /path/to/notion_random_page.py /path/to/config.json
   ```

2. Macのショートカットアプリで使用する場合は、シェルスクリプトアクションに以下を設定します。

   ```bash
   /path/to/python3 /path/to/notion_random_page.py /path/to/config.json
   ```

## 注意事項

- ショートカットアプリで実行する際は、正しいPython環境が指定されていることを確認してください。
- `requests`モジュールがインストールされている環境でスクリプトを実行してください。
