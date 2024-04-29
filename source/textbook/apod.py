import requests


def main():
    params = {"date": "2022-10-24", "api_key": "DEMO_KEY"}  # Python 3.11のリリース日
    url = "https://api.nasa.gov/planetary/apod"

    response = requests.get(url, params=params)
    data = response.json()

    print("タイトル", data["title"])
    print("日付", data["date"])
    print("URL: ", data["url"])


if __name__ == "__main__":
    main()
