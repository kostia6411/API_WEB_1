import requests
import os
from dotenv import load_dotenv


def main():
    load_dotenv()

    url_holidays = os.getenv("URL_HOLIDAYS")

    response = requests.get(url_holidays)
    response.raise_for_status()

    all_holidays = response.json()["response"]["holidays"]

    for holiday in all_holidays:
        name = holiday["name"]
        description = holiday["description"]
        month = holiday["date"]["datetime"]["month"]
        day = holiday["date"]["datetime"]["day"]
        print(f"Дата: {day}.{month}, Название праздника: {name}, Описание: {description}")


if __name__ == '__main__':
    main()