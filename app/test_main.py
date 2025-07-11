from app.main import get_human_age


def test_cat_and_dog_ages() -> None:
    result = get_human_age(14, 14)
    assert result == [0, 0]

    result = get_human_age(15, 15)
    assert result == [1, 1]

    result = get_human_age(23, 23)
    assert result == [1, 1]

    result = get_human_age(24, 24)
    assert result == [2, 2]

    result = get_human_age(27, 28)
    assert result == [2, 2]

    result = get_human_age(28, 29)
    assert result == [3, 3]
