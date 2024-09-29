import requests
from bs4 import BeautifulSoup


def main():
    url = 'https://docs.python.org/ja/3.12/library/functions.html'
    res = requests.get(url)
    content = res.content
    soup = BeautifulSoup(content, 'html.parser')
    
    # <table class="docutils">テーブルを見つける
    table = soup.find('table', class_='docutils')
    
    # テーブル内の全ての <a class="reference internal"> 要素を見つける
    functions = table.find_all('a', class_='reference internal')
    print('件数:', len(functions))
    
    for func in functions:
        func_name = func.text
        print(func_name)


if __name__ == '__main__':
    main()
