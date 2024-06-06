from app.main import get_human_age


def test_get_human_age():
    test_data = [
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 12, [2, 7]),
        (28, 12, [3, 7]),
        (24, 29, [2, 10]),
    ]

    for cat_age, dog_age, result in test_data:
        assert get_human_age(cat_age, dog_age) == result
