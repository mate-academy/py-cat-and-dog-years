import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (27, 28, [2, 2]),
        (100, 0, [21, 0]),
        (0, 100, [0, 17])
    ],
    ids=[
        "test must return zero list",
        "test list with number must return zero list",
        "test must return one age",
        "test must return two age for cat",
        "test must return three age for cat",
        "test must return age for cat",
        "test must return result for cat two",
        "test must check hundred age",
        "test cat zero, dog hundred"
    ]
)
def test_on_checks_ago(cat_age: int, dog_age: int, result: int) -> None:
    assert get_human_age(cat_age, dog_age) == result


def test_on_checks_len_list() -> None:
    assert len(get_human_age(13, 13)) == 2
