import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat,dog,result",
    [
        (0, 0, [0, 0]),
        (-27, 15, [0, 1]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ],
    ids=[
        "should return correct human age for cat:0 and dog:0",
        "should return correct human age for cat:-27 and dog:15",
        "should return correct human age for cat:14 and dog:14",
        "should return correct human age for cat:15 and dog:15",
        "should return correct human age for cat:23 and dog:23",
        "should return correct human age for cat:24 and dog:24",
        "should return correct human age for cat:27 and dog:27",
        "should return correct human age for cat:28 and dog:28",
        "should return correct human age for cat:100 and dog:100",

    ]
)
def test_correct_result(cat: int, dog: int, result: list) -> None:
    assert (get_human_age(cat, dog) == result)


@pytest.mark.parametrize(
    "cat,dog",
    [
        ("dog", "cat"),
        ([], ()),
        (14, "12"),
    ]
)
def test_age_not_integer(cat: str, dog: str) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat, dog)
