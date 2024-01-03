from app.main import get_human_age


def test_zero_cat_year() -> None:
    assert get_human_age(14, 0) == [0, 0], "0-14 cat years give 0 human year"


def test_1st_cat_year() -> None:
    assert (
        (get_human_age(15, 0) == [1, 0]) and (get_human_age(23, 0) == [1, 0])
    ), "15-23 cat years give 1 human year"


def test_2nd_cat_year() -> None:
    assert (
        (get_human_age(24, 0) == [2, 0]) and (get_human_age(27, 0) == [2, 0])
    ), "24-27 cat years give 2 human year"


def test_rest_cat_years() -> None:
    assert get_human_age(
        28, 0
    ) == [3, 0], "more 28 cat years give 3+ human year"


def test_zero_dog_year() -> None:
    assert get_human_age(0, 14) == [0, 0], "0-14 dog years give 0 human year"


def test_1st_dog_year() -> None:
    assert (
        (get_human_age(0, 15) == [0, 1]) and (get_human_age(0, 23) == [0, 1])
    ), "15-23 dog years give 1 human year"


def test_2nd_dog_year() -> None:
    assert (
        (get_human_age(0, 24) == [0, 2]) and (get_human_age(0, 28) == [0, 2])
    ), "24-28 dog years give 2 human year"


def test_rest_dog_years() -> None:
    assert get_human_age(
        0, 29
    ) == [0, 3], "more 29 dog years give 3+ human year"


if __name__ == "__main__":
    test_zero_cat_year()
    test_1st_cat_year()
    test_2nd_cat_year()
    test_rest_cat_years()
    test_rest_dog_years()
    test_1st_dog_year()
    test_2nd_dog_year()
    test_rest_dog_years()
    print("Everything passed")
