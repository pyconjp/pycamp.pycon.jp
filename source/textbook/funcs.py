import requests
from bs4 import BeautifulSoup


def main():
    url = 'https://docs.python.org/ja/3.10/library/functions.html'
    res = requests.get(url)
    content = res.content
    soup = BeautifulSoup(content, 'html.parser')
    functions = soup.find_all('dl', class_='py function')
    print('件数:', len(functions))
    for func in functions:
        func_name = func.dt.code.text

        # 上記記述だと@staticmethodの関数名が正しく取れないので、取りたい場合はこちら
        # func_name = func.dt.find_all('code', class_='sig-name')[0].text

        print(func_name)


if __name__ == '__main__':
    main()
