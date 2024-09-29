import requests
import random
import webbrowser

# Notion APIの設定
NOTION_API_KEY = 'YOUR API KEY'
DATABASE_ID = 'YOUR DATACASE ID'
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

if __name__ == '__main__':
    random_page = get_random_page()
    if random_page:
        page_url = display_page_info(random_page)
        webbrowser.open(page_url, new=2)  # new=2は新しいタブで開くオプション
    else:
        print('データベースにページがありません。')