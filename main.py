import requests
import os
from dotenv import load_dotenv


def main():
    load_dotenv()

    api_key = os.getenv("API_KEY")

    payload = {
        "api_key": api_key,
        "country": "ru",
        "year": "2025"
    }

    url = "https://calendarific.com/api/v2/holidays"

    response = requests.get(url, params=payload)
    response.raise_for_status()

    all_holidays = response.json()["response"]["holidays"]

    months = [
        "Января",
        "Февраля",
        "Марта",
        "Апреля",
        "Мая",
        "Июня",
        "Июля",
        "Августа",
        "Сентября",
        "Октября",
        "Ноября", 
        "Декабря"
    ]

    for holiday in all_holidays:
        name = holiday["name"]
        description = holiday["description"]
        month = holiday["date"]["datetime"]["month"]
        day = holiday["date"]["datetime"]["day"]
        print(f"Дата: {day} {months[month-1]}")
        print(f"Название праздника: {name}")
        print(f"Описание: {description}\n")


if __name__ == '__main__':
    main()