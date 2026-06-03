from src.counter_service import CounterService


def test_top_frequent_items(tmp_path):
    sample_file = tmp_path / "sample.txt"

    sample_file.write_text(
        "\n".join(
            [
                "apple",
                "apple",
                "banana",
                "apple",
                "orange",
                "banana",
                "banana",
            ]
        )
    )

    result = CounterService.top_frequent_items(str(sample_file))

    assert result[0] == ("apple", 3)
    assert result[1] == ("banana", 3)