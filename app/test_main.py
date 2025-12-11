import pytest


from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (1000, 1000, [246, 197]),
        (0, 0, [0, 0]),
        (-1, -1, [0, 0]),
        (15, 28, [1, 2]),

    ],
    ids=[
        "14 years for cat and dog",
        "15 years for cat and dog",
        "24 years for cat and dog",
        "28 years for cat and dog",
        "1000 years for cat and dog",
        "0 years for cat and dog",
        "-1 years for cat and dog",
        "different years for cat = 15 and dog = 28",
    ]
)
def test_general(cat_age: int, dog_age: int, result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result


def test_errors() -> None:
    with pytest.raises(TypeError):
        get_human_age("1", "1")
