from collections import Counter


class CounterService:
    @staticmethod
    def top_frequent_items(filepath: str, limit: int = 5):
        counter = Counter()

        with open(filepath, "r", encoding="utf-8") as file:
            for line in file:
                item = line.strip()

                if item:
                    counter[item] += 1

        return counter.most_common(limit)