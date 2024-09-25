import requests


def main():
    url = "https://swapi.info/api/films"

    response = requests.get(url)
    films = response.json()

    for film in films:
        print(
            "Episode "
            + str(film["episode_id"])
            + ": "
            + film["title"]
            + " ("
            + film["release_date"]
            + ")"
        )


if __name__ == "__main__":
    main()
