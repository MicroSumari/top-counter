import os

from dotenv import load_dotenv

from src.counter_service import CounterService

load_dotenv()


def run():
    file_path = os.getenv("FILE_PATH")

    items = CounterService.top_frequent_items(file_path)

    for item, count in items:
        print(f"{item}: {count}")


if __name__ == "__main__":
    run()