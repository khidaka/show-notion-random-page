import requests
import random
import webbrowser
import json
import sys

def load_config(config_path):
    with open(config_path, 'r') as config_file:
        return json.load(config_file)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python show_notion_random_page.py <config_file>")
        sys.exit(1)

    config_path = sys.argv[1]
    config = load_config(config_path)

    NOTION_API_KEY = config['NOTION_API_KEY']
    DATABASE_ID = config['DATABASE_ID']
    NOTION_VERSION = '2022-06-28'

    def get_random_page():
        url = f'https://api.notion.com/v1/databases/{DATABASE_ID}/query'
        headers = {
            'Authorization': f'Bearer {NOTION_API_KEY}',
            'Notion-Version': NOTION_VERSION,
            'Content-Type': 'application/json'
        }
        
        response = requests.post(url, headers=headers)
        if response.status_code != 200:
            raise Exception(f'APIリクエストエラー: {response.status_code}')
        
        pages = response.json()['results']
        if not pages:
            return None
        
        random_page = random.choice(pages)
        return random_page

    def display_page_info(page):
        title = page['properties']['名前']['title'][0]['text']['content']
        url = page['url']
        print(f'タイトル: {title}')
        print(f'URL: {url}')
        return url

    random_page = get_random_page()
    if random_page:
        page_url = display_page_info(random_page)
        webbrowser.open(page_url, new=2)
    else:
        print('データベースにページがありません。')